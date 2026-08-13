%global tl_name etbb
%global tl_revision 78931
%global tl_version 1.057

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	An expansion of Edward Tuftes ET-Bembo family
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/etbb
License:	mit lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etbb.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etbb.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Based on Daniel Benjamin Miller's XETBook, which expanded Tufte's
ETBook, the family name for the Bembo-like font family he commissioned
for his books, ETbb expands its features to include a full set of figure
styles, small caps in all styles, superior letters and figures, inferior
figures, a new capital Sharp S with small caps version, along with
macros to activate these features in LaTeX. Both otf and pfb are
provided.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from etbb:
Map ETbb.map
TL_DROPIN_EOF
