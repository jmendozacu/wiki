How to Install Magento 2 via Wizard
======================================

Installation process
---------------------

#. Download latest version at: https://www.magentocommerce.com/download
#. After download, you can upload to your server then extract it into xampp/htdocs/magento20
#. Open phpmyadmin and create database with name ‘magento20’
#. Open browser and go to page: http://localhost.com/magento20. You will auto redirect to http://localhost.com/magento20/setup/#/landing-install
	.. image:: https://lh5.googleusercontent.com/CM-a0qxaJHXdEftIApyeBIsjwx5U4b3SKRyrtHBipSpCcxOQKxD08-B-AoPZ9y4SzXi_Zk2CVRNW-1vP0WrF02VEdOG291rDhDHI9sllbmObj5BE2xC59bAI_SVz1Tk11Kpsk23R
#. Click **Agree and Setup Magento**
	.. image:: https://lh6.googleusercontent.com/VfxVRQ_VLu6pLdHr-iu7eyp8PgAv1s8-iJl8hzcNrs74FGtReG7MwU8h7aiE4P_mJwDURzvkYomtV96ySAAWkLsw4URG-4FqoNDVMzcEVhGB_RlGrDFkRDGgexC6F-Uhw9lzkfE9
#. Click **Start Readiness Check**
	.. image:: https://lh4.googleusercontent.com/D4ibVVWF9rzRvKA0Vyz1sQ_I-qRDjXgf56M_lBrtvkmf6z50v2cynZ1NhaXwfZ5mPq7BFfCpaUbP4VL-ronfdZ2vLqrAN7avccJd_C3i_hfLW12XbbJuLEfG4LgVF13nGYXa8xdw
#. Click **Next** and add your database information
	.. image:: https://lh5.googleusercontent.com/NkZD7qQz47p-kLt346iJ0_g2eavFA0jUnuJ7EtlQcoRg30EYrTL-OW65pYQ3vsjfNGK0qql3U7hUTiOFAlqM8sQbRNLo8ypuxjRDaRbXc9-Naj9-_vWJWskGrUyaASznZzk1uCRU
#. Click **Next** , you can change your store information
	.. image:: https://lh4.googleusercontent.com/Rhhk3YGslHj2FItOjBU41riQ9x2LcTq3XGSz1TEa9QeV5Uzb9O5lnwG6Da2OSSoMRUtra3_xcV35jr1upvEsfQ3UURv2dCXCNKegW0dp4hVcmkC2CiPne-eLXBSl1jWBn3I6GTef
#. Click **Next** to continue
	.. image:: https://lh3.googleusercontent.com/ULm0onLjpOYbR5pMDrPQfuAKsziBrjxr36qNyRQwAoD9UZHC5oMHN8_laV9BSoTRMUMa5CsErcRdlBqSYVGxFUZGKUcVg87ewu-UtZ4cBIJUhcgM3qxws2Y6T1PVEUzYJgeyKsaW
#. Click **Next** then Enter Admin Acount
	.. image:: https://lh5.googleusercontent.com/YNAT02dOm-7G7BiaKH6c-wa5FrQbWPM83eXYHSMe61ie1BErn50Z-yVSR9jgmdqsmy4TJp1MsM92NQ1JCIBCvq_96PMFxpJTP4S58IIZBoVNsvvby6BcAZBr5AYjQuyXdIn1QFIX
#. Click **Next**
	.. image:: https://lh3.googleusercontent.com/BCuUI28FgKzTbU0UZ5W5qbm3wnYQ_xYxYbvXTI6CBAo8MoS0Ctd9NOGNnQnPu_hoBi1f47knTVOsKIH8hWbUYVCMd52ci1aYrvLeQAIXJNBFie91UtA3mCmSbnejEqqFbc7t36oj
#. Click **Install Now**

	.. image:: https://lh4.googleusercontent.com/kvpDTMXcMqUm-73iMAAOOXbnxhKLzbQDw2O0E7ftYiX2qXw-o8dntxWimN7FR7_eAs29VOkKSsREW-FQ-QxrMbZVPlXFZDpqiZOVniklCpK5j2JjKpIvyk_H5jSHbGuktVV4bATM


	**Installing success**:

	.. image:: https://lh4.googleusercontent.com/oCV7ZblQsk-xtRLN9JzgXpQtgid36qxG9V2W--BZbjb_W-yqH5TVL4ItRc-f7A2d2C6zl3jCyOfXYlFf9mfqf7UOZdPej_w-WuV9mvKww6901MZ9bvis7QQTulZ6bBmgv05vppFU

If css/js/image are not loading
---------------------------------
You can change that behavior by doing the following


#. Open app/etc/di.xml and find the virtualType name="developerMaterialization" section. In that section you’ll find an item name="view_preprocessed" that needs to be modified or deleted. You can modify it by changing the contents from: ``Magento\Framework\App\View\Asset\MaterializationStrategy\Symlink`` to ``Magento\Framework\App\View\Asset\MaterializationStrategy\Copy``
#. Delete fields under pub/static to get rid of any existing symlinks. You can want to be careful not to delete the .htaccess file

This will solve your problems.
 
	**Home Page**
	 

	.. image:: https://lh3.googleusercontent.com/Wo76iRILMCUp6gzLJyPYcHKpOx4cdcbSiNmXTc_iIpPDa9aK2S5x5vsXLJXNreRyeWBzlHKIiJaI-fy1MiQr1JkFHDWRasTRCLPlDXUb2i-8zbJbDLa60DNMMFSw-9BZMTafWG04


	**Products Page**


	.. image:: https://lh4.googleusercontent.com/wW0nTLXCQ8He2t7S0xlPOe2iFKbhalhO8p0AjtVv9bAHL8cfFTkjMO6-6vz7AyjriaezRA_ho6ex2j2CrpL1n6isnKHbUCD0-lB4wtao1NM0S6wuDtvFzcfPNoM2mxjaWZrxoLfs


	**Admin**


	.. image:: https://lh6.googleusercontent.com/0BNfF-r0iloCLrEU_klP6QW686lbMO2NG_VvGojFrsMKWJKLYREnzwYIhvATc2EoTdf9JkK8oDrZptcEtEyKJt3BjOVfuwwX4eOz45qixBxRQgOAl5J6w1jdiX6Teb5j3M2s0EgO


Boost sales with `Magento One Step Checkout extension <https://www.magecheckout.com/magento-one-step-checkout.html>`_ and `Magento One Step Checkout <https://www.magentocommerce.com/magento-connect/one-step-checkout-37-28858.html>`_