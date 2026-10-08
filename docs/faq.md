# FAQ

<a id="h.p4aqrxgal5w4_l"></a>

## I have bought a new phone. How can I transfer my data to the new phone {#h.p4aqrxgal5w4}

If you have [aWallet Cloud](https://play.google.com/store/apps/details?id=org.awallet.cloud): see [FAQ Cloud](faq-cloud/index.md). 

If you have aWallet:

- Unlock aWallet in the old phone.
- On the main aWallet screen Press Menu | Backup data file and create a new folder. 

  - The menu button can be represented by 3 vertical dots at the top right corner on some Android phones. Other phones have a menu button located at the bottom corner represented by 3 horizontal lines.
  - Don't overwrite the existing backup file which sometimes corrupts the file and the file can't be unlocked.
- Use this [guide](https://support.google.com/android/answer/9064445) to connect the phone via a USB cable and copy the data.crypt file to your PC/Mac.

  - Make sure that the proper USB connection mode is selected:

    1. On your phone, tap the "Charging this device via USB" notification.
    2. Under "Use USB for" select File Transfer

- Install aWallet to your new phone using Google Play.
- Use this [guide](https://support.google.com/android/answer/9064445) to connect the phone via a USB cable and copy the data.crypt file from your old phone to a new created folder

  - Make sure that the proper USB connection mode is selected:

    1. On your phone, tap the "Charging this device via USB" notification.
    2. Under "Use USB for" select File Transfer
- In the aWallet main screen press Menu | Restore data file and choose the folder folder with the data.crypt file.
- Unlock aWallet using the password you have used on the old phone.

<a id="h.p66zpmd8mhys_l"></a>

## I have bought a new phone. How can I transfer my data to the new phone using aWallet Cloud {#h.p66zpmd8mhys}

First, install [aWallet Cloud](https://play.google.com/store/apps/details?id=org.awallet.cloud) to your old phone and import data from the free version:

1. Do backup in aWallet free: unlock the app, press the menu button, select the "Backup data file" option
2. Install (or reset) aWallet Cloud in the old phone
3. Select "Import existing aWallet data" on the second screen
4. Choose your cloud and account...

Then install [aWallet Cloud](https://play.google.com/store/apps/details?id=org.awallet.cloud) to your new phone and import data from the cloud:

1. Install (or reset) aWallet Cloud in the new phone
2. Select "Restore from cloud" on the second screen
3. Choose your cloud and account...

<a id="h.2a86ld1hnga3_l"></a>

## How to make a backup. Where is stored backup of the encrypted file {#h.2a86ld1hnga3}

Note: If you have aWallet Cloud you have data.crypt file backup in your own cloud account (Dropbox, Google Drive or WebDAV). You can ignore this question.

To create data backup unlock aWallet and in the aWallet home screen press menu | Backup data file and create a new folder.

Use this [guide](https://support.google.com/android/answer/9064445) to connect your phone via a USB cable and copy the data.crypt file to your PC/Mac.

- Make sure that the proper USB connection mode is selected:

  1. On your phone, tap the "Charging this device via USB" notification.
  2. Under "Use USB for" select File Transfer

NOTE:

- The backup file is NOT located in the micro SD card chip but is stored inside the phone in the external storage. Therefore make sure to copy the backup file outside the phone.

<a id="h.bagufcz1t8zz_l"></a>

## How do I restore data from backup? {#h.bagufcz1t8zz}

- Use this [guide](https://support.google.com/android/answer/9064445) to connect the phone via a USB cable and copy the data.crypt to a new folder.

  - Make sure that the proper USB connection mode is selected:

    - On your phone, tap the "Charging this device via USB" notification.
    - Under "Use USB for" select File Transfer
- In the aWallet main screen press Menu | Restore data file.

<a id="h.56k49qy8ubh_l"></a>

## How do I change my password? The option Change Password is grayed out {#h.56k49qy8ubh}

- Make sure aWallet is unlocked.

  - To access most features you have to unlock aWallet first using the current password.
- Press Menu | Change Password on the main screen.

<a id="h.axuqgikcsint_l"></a>

## If I forget my password. Is there a way to recover my data? {#h.axuqgikcsint}

- If you have another device that can be unlocked by fingerprint or Face ID you can [change the password](faq.md#h.56k49qy8ubh).
- Otherwise, the only way to unlock it is by using the correct password. All data is encrypted using the master password and the password is not stored anywhere in this case.
- If you want to reset aWallet so that you can start again from scratch, reinstall the app.

<a id="h.hll2qol93zl9_l"></a>

## I've changed the password but don't remember it. But I do remember my old password. Is there a way to recover my data? {#h.hll2qol93zl9}

- You can restore an older backup file to reset the old password.
- If you are using aWallet Cloud this is how to recover [older data from the cloud](faq-cloud/index.md#h.b0ndjboen6n).

<a id="h.trrlusy1bptz_l"></a>

## I changed my fingerprint in my phone and now can't access aWallet app with my fingerprint {#h.trrlusy1bptz}

- When a new fingerprint is added Android automatically deletes aWallet password stored in the secured KeyStore inside the phone. In this case, the only option is to remember the master password. Sorry.
- If you have another device with aWallet which you can currently unlock with the fingerprint it is possible to change the master password on this device. Please see [how to change the password](faq.md#h.56k49qy8ubh).

<a id="h.sxdetohau1m4_l"></a>

## I reset my phone, how can I recover my data in aWallet? {#h.sxdetohau1m4}

Note: If you have [aWallet Cloud](https://play.google.com/store/apps/details?id=org.awallet.cloud) you have the data.crypt file backup in your own cloud account (Dropbox, Google Drive or WebDAV). When you reinstall aWallet Cloud from Google Play select the "Restore from cloud" option in the initial screen. Ignore the steps below.

- It is necessary to have data.crypt file to recover your data.
- ! Never reset your phone if you didn't already have data.crypt file saved in your PC/Mac or cloud.
- Resetting the phone is like buying a new one. Please [see the steps](faq.md#h.p4aqrxgal5w4) on how to transfer data to a new phone.

<a id="h.6hb9fhsdr1yz_l"></a>

## I cannot find the Pro version in Google Play {#h.6hb9fhsdr1yz}

- There is no separate aWallet Pro version in Google Play. aWallet can be upgraded to get Pro features. Please see the question below on how this can be done.

<a id="h.r9sch8lsqb94_l"></a>

## How do I upgrade to Pro? {#h.r9sch8lsqb94}

- Open aWallet About dialog (press the Menu button | About). There is Upgrade to Pro button.

<a id="h.h3wlmitz9ikg_l"></a>

## I have upgraded to Pro, but cannot find the password generator {#h.h3wlmitz9ikg}

- To open Password Generator go to the Entry editor and press the pencil icon next to the hidden field. A hidden field is usually Password or Pin.
- Also, look at this video <https://www.youtube.com/watch?v=vdrOtAUdiqM> at 0:52 to see how to open the password generator.

<a id="h.v18ei8u6rzbf_l"></a>

## I have lost Pro upgrade {#h.v18ei8u6rzbf}

- To fix this try restarting the phone first.
- Pro features are associated with Google accounts in Google Play. Did not you recently remove some Google account from your phone? If yes add the account back to the phone.
- If you have multiple Google accounts in your phone remove the other accounts and once the issue is solved add these accounts back.
- Also, make sure your phone is connected to the Internet so that Google Play can refresh the license information. aWallet then remembers the license for 30 days offline.
- Background data for the Google Play Store app must be enabled as well. Please see https://support.google.com/googleplay/answer/1663315?hl=en

<a id="h.7ni4069xsxc_l"></a>

## I've imported data from CSV. How to split imported records into relevant categories? {#h.7ni4069xsxc}

- Just split the CSV file into multiple CSV files. aWallet will import them all at once to separate Categories. The name of each CSV file will become the name of each new Category.
- Please see also [CSV Import](documentation/index.md#h.59q1c0fbtxom).

<a id="h.d6jvp3dyvch8_l"></a>

## Password Generator is not available for new Category imported from CSV, only for existing Categories {#h.d6jvp3dyvch8}

- To enable Password Generator for any field, go to the "Category Editor" and mark any field in any category as "hidden" (using the checkbox with the "eye" icon). All hidden fields have Password Generator available automatically.
- When a new Category is imported from CSV none of its fields are hidden.
- If the same Category is imported from CSV again, all its hidden fields are retained. The custom category icon is retained as well.

<a id="h.w3ctiy9iv2n_l"></a>

## How to export data to CSV. Where are stored exported Categories in CSV? {#h.w3ctiy9iv2n}

- To export data to CSV make sure aWallet is unlocked and on the main screen press Menu | Export data to CSV and choose existing or create a new folder.

  - Use this [guide](https://support.google.com/android/answer/9064445) to connect the phone using a USB cable.

    - Make sure that the proper USB connection mode is selected:

      1. On your phone, tap the "Charging this device via USB" notification.
      2. Under "Use USB for" select File Transfer
  - !!! Note that CSV files are NOT encrypted and are accessible by many other apps from your phone. Therefore delete CSV files as soon as possible.

<a id="h.j11spxd08azz_l"></a>

## Cannot backup, "Backup data file" item is gray, can not be executed {#h.j11spxd08azz}

Note: If you have aWallet Cloud version you have data.crypt file backup in your cloud (Dropbox, Google Drive or WebDAV). You can ignore this question.

- Make sure aWallet is unlocked and the USB cable is unplugged.

<a id="h.jxdh7bymrgu6_l"></a>

## Cannot find data.crypt or CSV backup on SD card {#h.jxdh7bymrgu6}

- Note that the backup is NOT stored on the micro SD card removable chip but in the phone's external storage (also called USB memory).
- Use this [guide](https://support.google.com/android/answer/9064445) to connect the phone via a USB cable.

  - Make sure that the proper USB connection mode is selected:

    1. On your phone, tap the "Charging this device via USB" notification.
    2. Under "Use USB for" select File Transfer
- See also this post for more info about different storage types in Android phones.

<a id="h.j37qyronhx3q_l"></a>

## When I connect my phone to a PC using a USB cable I don't see data.crypt file or exported CSV files {#h.j37qyronhx3q}

- Use this [guide](https://support.google.com/android/answer/9064445) to connect the phone using a USB cable.

  - Make sure that the proper USB connection mode is selected:

    1. On your phone, tap the "Charging this device via USB" notification.
    2. Under "Use USB for" select File Transfer

<a id="h.afe5ivufql0o_l"></a>

## How to change the algorithm? {#h.afe5ivufql0o}

- The encryption algorithm is changed during password change. Please see [changing password](faq.md#h.56k49qy8ubh).

<a id="h.873delky28vi_l"></a>

## Can I copy record fields to the clipboard? {#h.873delky28vi}

- Yes. In the Entry Viewer, tap the Label and the Value will be copied into the clipboard. The label is to the left of the text value.
- It is also possible to long-press the value in the Entry Viewer to copy all or just part of the text.

  - Note that copying passwords to the Clipboard might be very dangerous. Every application from your phone can see ALL clipboard changes! And possibly send all texts from the clipboard out of your phone. Clearing the clipboard later maybe therefore too late. Never copy your sensitive passwords or PINs to the clipboard!

<a id="h.174rn8148ku_l"></a>

## How can I change the Category icon? {#h.174rn8148ku}

- In the Category Editor, touch the Category Icon and the screen for icon selection will open.

<a id="h.ws1uw9l7xlbq_l"></a>

## Is there a way to move entries from one category to another {#h.ws1uw9l7xlbq}

- Moving entries is not possible, unfortunately. The main reason is that categories may not be compatible in general. For e.g. an entry from the Credit Card category will not fit the Email category. There is a different number of fields and also field names don't match.
- If you imported data from a CSV file you can split the file into multiple CSV files and import them to aWallet. Each CSV file will create its own category.

<a id="h.93qie9jzaj2i_l"></a>

## Cannot find the menu button {#h.93qie9jzaj2i}

- The menu button is available on aWallet home screen.
- It can be represented by 3 vertical dots at the top or bottom right corner of the screen.
- Other phones have a physical menu button located at the bottom corner represented by 3 horizontal lines.

<a id="h.fy88ru68h70j_l"></a>

## Why the menu item "Reset aWallet" is available when aWallet is locked? {#h.fy88ru68h70j}

- It is available for the case when the user forgets the master password. Reset function deletes data but not aWallet settings.

  - If anybody gets access to the phone he/she can reinstall or uninstall any app. Or can open Android Settings / Apps / aWallet and press the "Delete data" button. In both cases, anyone can delete data from any of your installed apps. Therefore disabling this menu item would create a false sense of security.
  - The phone should be always secured by a lock screen PIN so that nobody can do wrong actions with it (e.g. send emails on your behalf, etc.).

<a id="h.ckw9zp3kn09d_l"></a>

## Is my data well protected? {#h.ckw9zp3kn09d}

- aWallet since Android 6 or later doesn't use any insecure permissions.
- Since aWallet original app has no access to the Internet, SMS, or other networks, it is impossible for the app to transfer data outside of your phone.

<a id="h.cun3mfjmnvny_l"></a>

## Can I send comments, bug reports, or ask for improvements? {#h.cun3mfjmnvny}

Yes. I welcome any suggestions. See the [Contact](contact.md) page.

<a id="h.af4gzllqvmp0_l"></a>

## What was the motivation to create this application? {#h.af4gzllqvmp0}

- I've been using a program called jWallet on my Nokia. It was a simple J2ME application that allowed me to have my private data always in my pocket. Later I've got Google Nexus S and wanted to have a similar app also in my new Android phone. So I decided to create aWallet for Android. I hope you enjoy aWallet as I do ;-)
