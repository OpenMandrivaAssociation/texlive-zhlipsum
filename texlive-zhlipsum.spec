%global tl_name zhlipsum
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.0
Release:	%{tl_revision}.1
Summary:	Chinese dummy text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/zhlipsum
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zhlipsum.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zhlipsum.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zhlipsum.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides an interface to dummy text in Chinese language,
which will be useful for testing Chinese documents. UTF-8, GBK and Big5
encodings are supported.

