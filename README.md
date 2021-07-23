In a pharmaceutical industry temperature,humidity and pressure is needed to be maintained in a particular range so as to get the desired product.

Suppose to measure these quantities an industry uses sensors and the data from these sensors is fed to a google sheet.
The data in the sheet is modified every 5 minutes.
Now responsibility is given to a human invigilator to continously check the redings every 5 minutes. 
But what if he forgets to check the reading. Due to this quality of a batch can be degraded and it can get rejected which can lead to loss for the comapany.

To solve this issue I have come up with a voice based industrial monitoring system. A voice application which will monitor the readings
of sensors from google sheet every 5 minutes and convey the current situation to the worker by voice.
By this the worker also do not need to watch the sheet continously and he can do some other task without the worry of watching the sheet 
every 5 minutes.

For this project I have created a python application. I have given it access to google sheets by creating a service account on google cloud platform
and downloading a credential file from there which I am using in my program.
To further bring my other skills to use I am running the program in Linux Virtual Machine.

I have taken ideal range of temperature, humidity and pressure as follows-

Temperature- 20-30 degree celsius

Humidity-    45-55 percent

Pressure-    12-18 pascals
