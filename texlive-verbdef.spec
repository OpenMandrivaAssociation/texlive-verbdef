%global tl_name verbdef
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Define commands which expand to verbatim text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/verbdef
License:	lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/verbdef.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/verbdef.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines a single command \verbdef (which has a *-form, like
\verb). \verbdef will define a robust command whose body expands to
verbatim text. By using commands defined by \verbdef, one can put
verbatim text into the arguments of commands; since the defined command
is robust, it doesn't matter if the argument is moving. (Full details of
syntax and caveats about use are in comments in the file itself.)

