# revision 17177
# category Package
# catalog-ctan /macros/latex/contrib/verbdef
# catalog-date 2010-03-09 13:13:30 +0100
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-verbdef
Version:	0.2
Release:	1
Summary:	Define commands which expand to verbatim text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/verbdef
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verbdef.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verbdef.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a single command \verbdef (which has a *-
form, like \verb). \verbdef will define a robust command whose
body expands to verbatim text. By using commands defined by
\verbdef, one can put verbatim text into the arguments of
commands; since the defined command is robust, it doesn't
matter if the argument is moving. (Full details of syntax and
caveats about use are in comments in the file itself.).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/verbdef/verbdef.sty
%doc %{_texmfdistdir}/doc/latex/verbdef/verbdef.pdf
%doc %{_texmfdistdir}/doc/latex/verbdef/verbdef.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
