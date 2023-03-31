%define modname	XML-Grove
%define modver	0.46alpha

Summary:	Provides the information set of parsed XML/HTML/SGML trees
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	18
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/XML/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel

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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%{perl_vendorlib}/XML/*
%{_mandir}/man3/*

