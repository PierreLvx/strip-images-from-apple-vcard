## Usage

`python strip-images-from-apple-vcard.py vCards.vcf clean.vcf`

## Credits

This repo is a fork of [a script authored by Mario Aeby](https://github.com/emeidi/strip-images-from-apple-vcard), with very minor fixes of mine.

## Purpose

Strips pictures from vCards .vcf exports from Apple's AddressBook to be imported into other VCF capable tools (e.g. RoundCube Webmail).

It may also be helpful if you experience slugishness in the Contacts app.

I was able to reduce a complete backup of my contacts in VCF format weighing 61 MB to 936 KB.

## Step by step

### AddressBook

1. Open AddressBook
2. Select all address book entries (Cmd-A)
3. AdressBook
4. Export...
5. Export vCard...
6. Save

### Shell

Python v3 compatible.

1. Switch to the directory containing this script and your VCF file
2. `./strip-images-from-apple-vcard.py vCards.vcf clean.vcf`
