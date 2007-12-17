%define module	XML-Grove
%define version	0.46alpha
%define release	%mkrel 8

Summary:	Provides the information set of parsed XML/HTML/SGML trees
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
Url:		http://www.cpan.org
BuildRequires:	perl-devel
Requires:	perl
BuildArch:	noarch

%description
The XML::Grove Perl module provides simple access to the information
set of parsed XML, HTML, or SGML instances using a tree of Perl
hashes.  This package also includes several extensions to XML::Grove
that provide the following:

   - returning element contents as a string
   - returning element contents as XML, HTML, or Canonical XML
   - processing entire groves using the visitor pattern
   - processing entire groves using PerlSAX
   - running a filter over all nodes in the grove
   - substituting values into an XML template grove
   - indexing a grove by ID or other attributes
   - accessing elements and objects via URL-like paths
   - create grove objects using an easy shorthand

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%{_mandir}/*/*
%{perl_vendorlib}/XML/*


