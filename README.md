# sURL
Simple URL shortener

This is a simple URL shortener app.

I used python 3.5.1 and Flask for server. Frontend is made using Bootstrap (files in `static` folder)

## Implementation under WSGI:
WSGI stands for Web Server Gateway Interface. Actually, it's Python Web Server Gateway Interface, because WSGI is a Python standard, born as a PEP (Python Enhancement Proposal) from the need of a simple and universal interface between web servers and web applications or frameworks (Flask, Django, Bottle and so forth).

WSGI has to be implemented on both server and framework sides in order to use its interface so that web server will know how to communicate with web application, and how scripts within the web application can be chained together to process one request.

On server side, in Apache implementation is made using configuration files that specify where an application should be imported from, and how URL requests are passed (sort of URL mapping).

MOD_WSGI shoul be installed in order to use WSGI with Apache. Just run in terminal:
`apt-get install libapache2-mod-wsgi`

The first route we need to declare is the WSGI application. If we would like to point our app at the root of web server (eg. http://domain.com), we use:
`WSGIScriptAlias / /var/www/surl/surl.wsgi`

Instead, if we would like to make it available at a suburl (eg. http://domain.com/ourapp), we declare as:

`WSGIScriptAlias /ourapp /var/www/surl/surl.wsgi`

We need to declare permissions; under previous line, add:
```
WSGIScriptAlias / /var/www/surl/surl.wsgi

<Directory /var/www/surl>
	Order deny, allow
	Allow from all
</Directory>
```
Add a few more directories:

```
WSGIScriptAlias / /var/www/surl/surl.wsgi

<Directory /var/www/surl>
	Order deny, allow
	Allow from all
</Directory>
```

## Azure config

Go to aka.ms/webpi-azps

Opening WindowsAzurePowershellGet.3f.3f.3fnew.exe

Save file - Run
This will install Microsoft Web Platform Installer 5.0

Click Install
Click I Accept
Microsoft Azure PowerShell will be installed

After installation is finished, click Exit

A reboot is required.

[Win]+[R]
powershell_ise.exe

Will open Windows PowerShell ISE (Integrated Scripting Environment)


In order to see current mode ('arm' for resource manager and 'asm' for service management), type:

`PS C:\Users\Razvan Cristea> azure config --help`
It should return:
 ```
 Current Mode: asm (Azure Service Management)

PS C:\Users\Razvan Cristea> Login-AzureRMAccount


Environment           : AzureCloud
Account               : razvan.cristea@live.com
TenantId              : efc8ca57-8d5f-48d9-9f17-e0400de45748
SubscriptionId        : 80f825a3-14c3-4511-bcc4-b1e356e31aac
CurrentStorageAccount : 
```
A new windows will pop out - enter credentials. In order to see your subscription, type:
```
PS C:\Users\Razvan Cristea> Get-AzureRmSubscription


SubscriptionName : Free Trial
SubscriptionId   : 80f825a3-14c3-4511-bcc4-b1e356e31aac
TenantId         : efc8ca57-8d5f-48d9-9f17-e0400de45748
State            : Enabled
```
We have to select it:
```
PS C:\Users\Razvan Cristea> Select-AzureRmSubscription -SubscriptionName "Free Trial"


Environment           : AzureCloud
Account               : razvan.cristea@live.com
TenantId              : efc8ca57-8d5f-48d9-9f17-e0400de45748
SubscriptionId        : 80f825a3-14c3-4511-bcc4-b1e356e31aac
CurrentStorageAccount : 

PS C:\Users\Razvan Cristea> Add-AzureAccount -Tenant efc8ca57-8d5f-48d9-9f17-e0400de45748

Id                      Type Subscriptions                        Tenants                         
--                      ---- -------------                        -------                         
razvan.cristea@live.com User 80f825a3-14c3-4511-bcc4-b1e356e31aac {efc8ca57-8d5f-48d9-9f17-e040...



PS C:\Users\Razvan Cristea> Get-AzureRmSubscription ñSubscriptionName "Free Trial" | Select-AzureRmSubscription


Environment           : AzureCloud
Account               : razvan.cristea@live.com
TenantId              : efc8ca57-8d5f-48d9-9f17-e0400de45748
SubscriptionId        : 80f825a3-14c3-4511-bcc4-b1e356e31aac
CurrentStorageAccount : 

PS C:\Users\Razvan Cristea> New-AzureReservedIP -Location "West Europe" -ReservedIPName ubuntuIP -ServiceName ubuntu14-uv7811tw

OperationDescription OperationId                          OperationStatus
-------------------- -----------                          ---------------
New-AzureReservedIP  cfc4db85-daa8-9638-9da5-660fa89e3d49 Succeeded 
```
If IP already exists, and we want to allocate it to existing cloud service, containing our VM, type:
```
PS C:\Users\Razvan Cristea> Set-AzureReservedIPAssociation -ReservedIPName ubuntuIP -ServiceName ubuntuserver-a46d287e

OperationDescription           OperationId                          OperationStatus
--------------------           -----------                          ---------------
Set-AzureReservedIPAssociation a988a5b5-e990-a883-83cd-65e3f32eb8d3 Succeeded      
```
