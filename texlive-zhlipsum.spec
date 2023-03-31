Name:		texlive-zhlipsum
Version:	54994
Release:	2
Summary:	Chinese dummy text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/zhlipsum
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zhlipsum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zhlipsum.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zhlipsum.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an interface to dummy text in Chinese
language, which will be useful for testing Chinese documents.
UTF-8, GBK and Big5 encodings are supported.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/zhlipsum
%{_texmfdistdir}/tex/latex/zhlipsum
%doc %{_texmfdistdir}/doc/latex/zhlipsum

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
