# IISER Pune Online Semester Dashboard

A Links page for Online Semesters of IISER Pune

Example Website: https://thereconpilot.github.io/iiserp-sem6

This project is a template website for hosting the various links that
are used during an online semester. It's a fairly simple layout and
design made using Bootstrap but it turns out to be extremely useful.

## How To Use

1. Fork this repo.
2. Create a Google Sheet containing all the relevant data of the course
    details and links. This is typically crowd-sourced to the whole batch.
    The sheet can be downloaded directly as CSV to the `data` directory.
    This can be automated by the google sheet API script in the repo
    (requires a google oauth account).
    An example is [Spring 2021 Datasheet][Sheet Link]
2. Run the `main.py` script. This uses [jinja2][Jinja2 Docs] to put all
    the data in a template from the `templates` directory.
3. Enable GitHub Pages for your repo.

## Troubleshooting

1. The `iiserid` column for an instructor refers to the number at
    the end of their page on the IISER Pune website. For example:
    for Bhas Bapat the url is `https://www.iiserpune.ac.in/people/faculty-details/135`
    so `iiserid = 135`. This column serves as the main index in the
    instructors datasheets, so it is very important to make sure that
    it exists for each instructor and that it is unique. If there is no
    such page for an instructor, make up a number but make sure it is
    not used for any other professor (starting from 1000 can be a good
    idea for such cases). 

## Contributing

### Help with Maintaining Data

You will be keeping the links up to date. Get in touch with us to help!
Or simply update things on the sheet and let us know, and we would update
the site.

### Contribute to the Site

This site is made with Neon Glow, a Bootstrap theme, and Jinja2 for templates.

Follow the standard contributing procedure.

- Fork this repository
- Create your branch: `git checkout -b my-feature-branch`
- Commit your changes: `git commit -am "Commit message"`
- Push to the branch: `git push origin my-feature-branch`
- Submit a Pull Request

### Developing
- Make changes in templates
- Use the `google-sheet-api.py` to fetch data from the sheet
- Run `python3 main.py` to generate pages

## Contact Us

- [Aditya Chincholi](mailto:aditya.chincholi@students.iiserpune.ac.in)
- [Purva Parmar](mailto:purva.parmar@students.iiserpune.ac.in)

Or contact us on WhatsApp, or Discord, or wherever you can find us.


[Sheet Link]: https://docs.google.com/spreadsheets/d/1wsEatRyeX6Vx27HB3rcpKb3E7nwzWup-3u45LuiRsyA/edit?usp=sharing
[Jinja2 Docs]: https://jinja.palletsprojects.com/en/3.0.x/
