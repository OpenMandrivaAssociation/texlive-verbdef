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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package defines a single command \verbdef (which has a *-
form, like \verb). \verbdef will define a robust command whose
body expands to verbatim text. By using commands defined by
\verbdef, one can put verbatim text into the arguments of
commands; since the defined command is robust, it doesn't
matter if the argument is moving. (Full details of syntax and
caveats about use are in comments in the file itself.).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/verbdef/verbdef.sty
%doc %{_texmfdistdir}/doc/latex/verbdef/verbdef.pdf
%doc %{_texmfdistdir}/doc/latex/verbdef/verbdef.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
