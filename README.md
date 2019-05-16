# bamboo-contact-sheet

A quick and dirty way to create an office contact sheet from Bamboo HR

![output](https://github.com/infinityworks/bamboo-contact-sheet/blob/master/output.png?raw=true)

## Getting started

To run this yourself, you'll need -

1. Python 3.x or higher
2. A Bamboo HR API key with permissions to retrieve the employee directory
3. PyBambooHR

Once you have a Bamboo HR API key and Python installed, run:

```
pip install PyBambooHR
bamboo-contact-sheet.py <your-bamboo-hr-api-key> location
```

## Changing the output

Changing the contact sheet formatting and styling can be done by editing the template.html and re-running the script. `<!--content-->` in template.html is replaced with the content from Bamboo HR.

Additional fields, such as phone number and email address, can be easily added if desired.

## Contributing

If you'd like to contribute, please do - submit a pull request when you're ready.
