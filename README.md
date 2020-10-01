# blacklight-cli

> Use [Blacklight](https://themarkup.org/blacklight) in your terminal

## Table of Contents

- [What's Blacklight?](#whats-blacklight)
- [Dependency](#dependency)
- [Usage](#usage)
  - [Example](#example)

## What's Blacklight?

Quote from [Blacklight](https://themarkup.org/blacklight) website: "...Blacklight is a real-time website privacy inspector. It will scan website and reveal the specific user-tracking technologies on the site—and who’s getting your data. You may be surprised at what you learn..."\_

## Dependency

- [requsts](https://requests.readthedocs.io/en/master/user/install/#install)

## Usage

```bash
$ ./blacklight.py "<url>"
```

### Example

```bash
$ ./blacklight.py 'kevcui.github.io'
> Inspection result:
  0 No ad trackers found on this site.
  0 Third-party cookies not found.
  0 Tracking that evades cookie blockers wasn't found.
  0 Session recording services not found on this website.
  0 We did not find this website capturing keystrokes.
  0 Facebook Pixel not found on this website.
  0 Google Analytics' "remarketing audiences" feature not found.
```

```bash
$ ./blacklight.py 'www.nytimes.com'
> Inspection result:
  10 Ad trackers found on this site.
  7 Third-party cookies were found.
  0 Tracking that evades cookie blockers wasn't found.
  0 Session recording services not found on this website.
  0 We did not find this website capturing keystrokes.
  0 Facebook Pixel not found on this website.
  ! This site allows Google Analytics to follow you across the internet.

> Ad-tech companies:
  Adobe: everesttech.net
  Alphabet: ampproject.org, doubleclick.net, google-analytics.com, google.com, googlesyndication.com, googletagmanager.com, gstatic.com
  comScore: scorecardresearch.com
  Criteo: criteo.com, criteo.net
  Microsoft: bing.com
  Oracle: bkrtx.com, bluekai.com
```

---

<a href="https://www.buymeacoffee.com/kevcui" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-orange.png" alt="Buy Me A Coffee" height="60px" width="217px"></a>