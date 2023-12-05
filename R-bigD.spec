#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: c1050fe
#
Name     : R-bigD
Version  : 0.2.0
Release  : 1
URL      : https://cran.r-project.org/src/contrib/bigD_0.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bigD_0.2.0.tar.gz
Summary  : Flexibly Format Dates and Times to a Given Locale
Group    : Development/Tools
License  : MIT
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
make sense. Parses dates, times, and date-times in various formats
    (including string-based ISO 8601 constructions). The formatting syntax gives
    the user many options for formatting the date and time output in a precise
    manner. Time zones in the input can be expressed in multiple ways and there
    are many options for formatting time zones in the output as well. Several of
    the provided helper functions allow for automatic generation of locale-aware
    formatting patterns based on date/time skeleton formats and standardized
    date/time formats with varying specificity.

%prep
%setup -q -n bigD

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701735006

%install
export SOURCE_DATE_EPOCH=1701735006
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/bigD/DESCRIPTION
/usr/lib64/R/library/bigD/INDEX
/usr/lib64/R/library/bigD/LICENSE
/usr/lib64/R/library/bigD/Meta/Rd.rds
/usr/lib64/R/library/bigD/Meta/features.rds
/usr/lib64/R/library/bigD/Meta/hsearch.rds
/usr/lib64/R/library/bigD/Meta/links.rds
/usr/lib64/R/library/bigD/Meta/nsInfo.rds
/usr/lib64/R/library/bigD/Meta/package.rds
/usr/lib64/R/library/bigD/NAMESPACE
/usr/lib64/R/library/bigD/NEWS.md
/usr/lib64/R/library/bigD/R/bigD
/usr/lib64/R/library/bigD/R/bigD.rdb
/usr/lib64/R/library/bigD/R/bigD.rdx
/usr/lib64/R/library/bigD/R/sysdata.rdb
/usr/lib64/R/library/bigD/R/sysdata.rdx
/usr/lib64/R/library/bigD/help/AnIndex
/usr/lib64/R/library/bigD/help/aliases.rds
/usr/lib64/R/library/bigD/help/bigD.rdb
/usr/lib64/R/library/bigD/help/bigD.rdx
/usr/lib64/R/library/bigD/help/paths.rds
/usr/lib64/R/library/bigD/html/00Index.html
/usr/lib64/R/library/bigD/html/R.css
/usr/lib64/R/library/bigD/tests/testthat.R
/usr/lib64/R/library/bigD/tests/testthat/test-dates_times.R
/usr/lib64/R/library/bigD/tests/testthat/test-fdt_locales.R
/usr/lib64/R/library/bigD/tests/testthat/test-time_zones.R