How to setup cronjob in Magento
===============================


What is cron or a cronjob?
------------------------------------------------------------------

Cronjob is a time-based job scheduler in Unix-like computer operating systems. Cron enables users to schedule jobs (commands or shell scripts) to run periodically at certain times or dates. It is commonly used to automate system maintenance or administration. According to Wikipedia.


Why do we need a cronjob in Magento? Because some tasks need to be automated - you don't really want to refresh the catalog index in Magento every couple of minutes, do you?

Magento uses the cron.php file sitting inside the root directory of Magento to manage and dispatch cronjobs. The cron.php script basically executes the internal Magento cronjob manager, managing which and when cronjobs are executed. 

Setting up the Magento cronjob using shell access
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the crontab file to set up the cronjob. The crontab manages which and when cronjobs are run on the server::

	crontab -e

Now, go to the end of the last line in the cron tab file and press enter to create a new line. 
Enter the following line and replace YOURDOMAIN.com and PATH_TO_MAGENTO with the URL of the root directory of your Magento installation::

	*/5 * * * * wget -O /dev/null -q http://www.YOURDOMAIN.com/PATH_TO_MAGENTO/cron.php > /dev/null


.. important:: It is very important that the cron.php file of Magento gets executed every five minutes. Do not change this to a longer interval.

Save the cron tab using CTRL+X, enter y to save the changes and press enter. The following message should be displayed: 

Setting up the Magento cronjob using cPanel, Confixx, Plesk, ...
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you've got access to a server control panel, setting up the cronjob is as easy as going to the Cronjob Manager inside the control panel. Make sure no other cronjob has been set up calling the cron.php file of Magento, and if that's the case, remove it before adding this cronjob. Add a cronjob with the following parameters:

- Minute: */5 
- Hour: *
- Day: *
- Month: *
- Weekday: *
- Command: ``wget -O /dev/null -q http://www.YOURDOMAIN.com/PATH_TO_MAGENTO/cron.php > /dev/null`` 




Boost sales with `Magento One Step Checkout extension <https://www.magecheckout.com/magento-one-step-checkout.html>`_ and `Magento One Step Checkout <https://www.magentocommerce.com/magento-connect/one-step-checkout-37-28858.html>`_