Name:		texlive-etbb
Version:	61872
Release:	2
Summary:	An expansion of Edward Tufte's ET-Bembo family
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/etbb
License:	mit lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etbb.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etbb.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Based on Daniel Benjamin Miller's XETBook, which expanded
Tufte's ETBook, the family name for the Bembo-like font family
he commissioned for his books, ETbb expands its features to
include a full set of figure styles, small caps in all styles,
superior letters and figures, inferior figures, a new capital
Sharp S with small caps version, along with macros to activate
these features in LaTeX. Both otf and pfb are provided.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/etbb
%{_texmfdistdir}/fonts/vf/public/etbb
%{_texmfdistdir}/fonts/type1/public/etbb
%{_texmfdistdir}/fonts/tfm/public/etbb
%{_texmfdistdir}/fonts/opentype/public/etbb
%{_texmfdistdir}/fonts/map/dvips/etbb
%{_texmfdistdir}/fonts/enc/dvips/etbb
%{_texmfdistdir}/fonts/afm/public/etbb
%doc %{_texmfdistdir}/doc/fonts/etbb

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
