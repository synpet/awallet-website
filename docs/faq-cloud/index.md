# FAQ Cloud

<a id="h.gynmufaemhb_l"></a>

## I have bought a new phone. How can I transfer my data to the new phone? {#h.gynmufaemhb}

1. Install aWallet Cloud to your new phone.

   - Use the same Gmail account in Google Play so you don't have to purchase it again.
2. Select "Restore from cloud" on the second initial screen.
3. Select cloud (Dropbox, Google Drive or WebDAV) you've used in the old phone, press OK.
4. Choose your cloud account email (the same as on the old phone) and allow aWallet to be linked with the selected cloud.

   - Note: If you already installed aWallet Cloud it is necessary to either reinstall it (or reset it) to see the options on the second initial screen.

<a id="h.81dti22tsyaz_l"></a>

## I got aWallet Cloud app. How can I import data from aWallet free app? {#h.81dti22tsyaz}

Please do not uninstall the free aWallet till you finish the rest of these steps!

- Open aWallet Cloud, and if you've initialized it already press Menu | Reset aWallet (or just reinstall aWallet Cloud).
- In the initialization screen select "Import existing aWallet data".
- You should see dialog: "Data restored from: data.crypt".
- On the next screen select either Dropbox, Google Drive or WebDAV, press OK.
- Choose your cloud account, and allow aWallet Cloud to be linked with the selected cloud.
- Once you successfully transfer data to aWallet Cloud you can uninstall the free version.

<a id="h.d4hl0sy8z466_l"></a>

## I've imported data to aWallet Cloud from existing aWallet app, should I keep both versions of aWallet? {#h.d4hl0sy8z466}

- aWallet Cloud and aWallet are independent applications. You can uninstall aWallet original.

<a id="h.32qe7q9odnf_l"></a>

## I bought the Cloud version to synchronize phone and tablet but I can't seem to figure out how to do that {#h.32qe7q9odnf}

- Install aWallet Cloud on the phone
- Install aWallet Cloud on the tablet

  - If you have already installed aWallet Cloud on the tablet then reinstall it (or reset it by pressing Menu | Reset aWallet)
- In the initial screen select "Restore from cloud"
- Choose your existing Cloud account. Allow linking with aWallet Cloud if you are asked to.

<a id="h.36534hg0xs7f_l"></a>

## Can aWallet Cloud work offline? I don't have access to the internet at the work {#h.36534hg0xs7f}

- aWallet Cloud doesn't need to have access to the internet to operate. It works offline the same way as aWallet free/original. It only will not synchronize data with the cloud while it is offline. Data will synchronize when you use aWallet Cloud online again.

<a id="h.ma9211yc4x75_l"></a>

## When I buy aWallet Cloud, can I use it with all my devices for a single purchase? {#h.ma9211yc4x75}

- Yes if these devices are using the same app store. Purchases are not shared between independent app stores.

<a id="h.oxs709vbwme3_l"></a>

## Is the price a one-time payment or a monthly fee? {#h.oxs709vbwme3}

- It is a one-time payment

<a id="h.n46lukwpmel3_l"></a>

## How can I change my cloud account? {#h.n46lukwpmel3}

1. Unlock aWallet Cloud
2. Press the menu button on the home screen
3. Choose Settings / Cloud
4. Select the cloud (Dropbox, Google Drive or WebDAV)
5. Choose your cloud user account

Note: To unlink aWallet Cloud from existing Dropbox account use this page: <https://www.dropbox.com/account/connected_apps>

<a id="h.b0ndjboen6n_l"></a>

## How can I restore the older version of data.crypt file from the cloud? {#h.b0ndjboen6n}

If you use Google Drive please see [Restore Google Drive revision](restore-google-drive-revision.md)

If you use Dropbox:

- Open aWallet Dropbox folder in the desktop web browser: <https://www.dropbox.com/home/Apps/aWallet%20Cloud>
- Click on the 3 dots button to the right of the data.crypt file and select the "Version history" option
- Choose an older version and click its "Restore" button
- Open aWallet Cloud in your phone or tablet and press the synchronize button on the home screen
- aWallet Cloud will download the restored revision

<a id="h.xqzk0oux2vso_l"></a>

## I'm getting an error: No data was downloaded from cloud. But the data.crypt file is in the cloud {#h.xqzk0oux2vso}

- When Google Drive is concerned... this can happen if you copy the data.crypt file to the cloud manually. In this case, aWallet cannot see the file because it can only see files it has created itself in Google Drive. aWallet doesn't have permission to see or read other files.
- If you use Dropbox... it stores application data in specific folders e.g. in "Dropbox/Apps/aWallet Cloud". aWallet can access files only within this folder after it gets the necessary permission. Therefore let aWallet create this file itself. Otherwise, aWallet may not be allowed to see this file.

<a id="h.piuaoa52sxgz_l"></a>

## I've changed phones but aWallet Cloud contains no data {#h.piuaoa52sxgz}

- Most probably aWallet Cloud was initialized with the "Create new data" option which created empty data in the cloud and overwritten the existing data. The proper option to restore data from the cloud is "Restore from cloud".
- This can be resolved by [restoring an older version](index.md#h.b0ndjboen6n) of the data.crypt file in the cloud.

<a id="h.t4bd3pdya8d2_l"></a>

## During synchronization aWallet gives "Error talking to cloud" message {#h.t4bd3pdya8d2}

- There is something wrong with the cloud connection. It is most likely a temporary network problem which should be solved automatically. If not try restarting your phone.
- Check if the cloud is not full.
- Also, make sure you are not connecting through a network that blocks connections to clouds (e.g. some company WiFi networks or some mobile networks when data plan is reached).

<a id="h.so2ojmg58vgb_l"></a>

## Can you explain aWallet Cloud Android permissions? {#h.so2ojmg58vgb}

- Read the contents of your USB storage

  - Needed for importing data.crypt file from the free version
- View network connections / Full network access

  - Needed for the cloud network connection
- Google Play license check

  - To check the Google Play app license

<a id="h.ppwxjbpk85fq_l"></a>

## Can not open data.crypt file to see passwords {#h.ppwxjbpk85fq}

- The data.crypt file backup is encrypted and can't be opened directly. aWallet Cloud reads and writes it automatically.
- The backup in the cloud is useful in the situation you lose your phone or if it stops working. In this case, you can install aWallet Cloud to a new phone and choose "Restore from Cloud" in the initialization screen.
- The cloud backup is also useful if you want to keep aWallet data synchronized in multiple Android or iOS devices automatically.

<a id="h.6hbeug4pk6z_l"></a>

## Purchased aWallet Cloud from Play. When try to synchronize, get message: aWallet Cloud licence not verified {#h.6hbeug4pk6z}

- Try restarting the phone first.
- Licenses are associated with Google accounts in Google Play. Did not you recently remove some Google account from your phone?
- Did not you reinstall aWallet Cloud using some backup software instead of from Google Play?
- Make sure your phone is connected to the Internet so that Google Play can refresh license information. aWallet then remembers the license for 30 days offline.
- Background data for the Google Play Store app must be enabled. Please see <https://support.google.com/googleplay/answer/1663315?hl=en>
- If it does not help reinstall aWallet Cloud from Google Play and choose the "Restore from cloud" option on the second initial screen.
- If you still have problems, please contact the support by email.
