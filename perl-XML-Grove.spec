%define upstream_name	 XML-Grove
%define upstream_version 0.46alpha

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Provides the information set of parsed XML/HTML/SGML trees
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
make

%install
%makeinstall_std

%files
%{_mandir}/*/*
%{perl_vendorlib}/XML/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.460.0alpha-5mdv2012.0
+ Revision: 765843
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.460.0alpha-4
+ Revision: 764340
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.460.0alpha-3
+ Revision: 667421
- mass rebuild

* Tue Jan 19 2010 Pascal Terjan <pterjan@mandriva.org> 0.460.0alpha-2mdv2011.0
+ Revision: 493739
- Rebuild to get the version right

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.460.0-1mdv2010.0
+ Revision: 408238
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.46alpha-10mdv2009.0
+ Revision: 224623
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.46alpha-9mdv2008.1
+ Revision: 180656
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 0.46alpha-8mdv2007.0
+ Revision: 108411
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-XML-Grove

* Mon Jan 10 2005 Stefan van der Eijk <stefan@mandrake.org> 0.46alpha-7mdk
- upload to contrib

