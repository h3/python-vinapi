python-vinapi
=============

A python client for Vin API.


Usage
-----

Checking your account status:

.. code-block:: python

    from vinapi import VinApi
    
    vin = VinApi("APIKEYGOESHERE")

    vin.status()
    {u'account-holder-since': u'2013-02-16',
     u'in-good-standing': u'true',
     u'total-spent': u'0',
     u'vins-freely-added-to-account': u'20',
     u'vins-purchased': u'0',
     u'vins-remaining': u'12',
     u'vins-used': u'8'}

Get summary for a VIN:

.. code-block:: python

    vin.find("1GKEV13728J123735", complete=False)
    {u'body-style': u'SPORT UTILITY 4-DR',
     u'country': u'UNITED STATES',
     u'engine-type': u'3.6L V6 DOHC 24V',
     u'make': u'GMC',
     u'model': u'Acadia',
     u'transmission': u'6-Speed Automatic Overdrive',
     u'vin': u'1GKEV13728J123735',
     u'year': u'2008'}

Get complete information for a VIN:

.. code-block:: python

    vin.find("1GKEV13728J123735")

    {u'abs-brakes': u'Standard',
     u'adjustable-foot-pedals': True,
     u'air-conditioning': u'Standard',
     u'alloy-wheels': u'Standard',
     u'am-fm-radio': u'Standard',
     u'anti-brake-system': u'4-Wheel ABS',
     u'automatic-headlights': u'Standard',
     u'automatic-load-leveling': True,
     u'body-style': u'SPORT UTILITY 4-DR',
     u'cargo-area-cover': u'Optional',
     u'cargo-area-tiedowns': True,
     u'cargo-length': u'in.',
     u'cargo-net': u'Optional',
     u'cargo-volume': u'25.50 cu.ft.',
     u'cassette-player': True,
     u'cd-changer': u'Optional',
     u'cd-player': u'Standard',
     u'child-safety-door-locks': u'Standard',
     u'chrome-wheels': True,
     u'city-mpg': u'16 miles/gallon',
     u'country': u'UNITED STATES',
     u'cruise-control': u'Standard',
     u'curb-weight': u'lbs',
     u'daytime-running-lights': u'Standard',
     u'dealer-invoice': u'$29,700 USD',
     u'deep-tinted-glass': u'Standard',
     u'depth': u'in.',
     u'destination-charge': u'$735 USD',
     u'driveline': u'all-wheel drive',
     u'driver-airbag': u'Standard',
     u'driver-multi-adjustable-power-seat': u'Optional',
     u'dvd-player': u'Optional',
     u'electrochromic-exterior-rearview-mirror': True,
     u'electrochromic-interior-rearview-mirror': True,
     u'electronic-brake-assistance': True,
     u'electronic-parking-aid': u'Optional',
     u'engine-type': u'3.6L V6 DOHC 24V',
     u'exterior-color': u'Blue/Gold Crystal Metallic, Carbon Black Metallic, Deep Blue Metallic, Dark Crimson Metallic, Gold Mist Metallic, Liquid Silver Metallic, Medium Brown Metallic, Platinum Ice, Red Jewel Tintcoat, Summit White, White Diamond Tricoat',
     u'first-aid-kit': True,
     u'fog-lights': u'Standard',
     u'four-wd-awd': u'Standard',
     u'front-air-dam': u'Standard',
     u'front-brake-type': u'Disc',
     u'front-cooled-seat': True,
     u'front-headroom': u'40.40 in.',
     u'front-heated-seat': True,
     u'front-hip-room': u'57.80 in.',
     u'front-legroom': u'41.30 in.',
     u'front-power-lumbar-support': True,
     u'front-power-memory-seat': True,
     u'front-shoulder-room': u'61.90 in.',
     u'front-side-airbag': u'Standard',
     u'front-side-airbag-with-head-protection': True,
     u'front-split-bench-seat': True,
     u'front-spring-type': '',
     u'front-suspension': u'Ind',
     u'full-size-spare-tire': True,
     u'genuine-wood-trim': True,
     u'glass-rear-window-on-convertible': True,
     u'ground-clearance': u'7.40 in.',
     u'heated-exterior-mirror': u'Standard',
     u'heated-steering-wheel': True,
     u'high-intensity-discharge-headlights': True,
     u'highway-mpg': u'22 miles/gallon',
     u'interior-trim': u'Ebony Cloth Interior, Light Titanium Cloth Interior',
     u'interval-wipers': u'Standard',
     u'keyless-entry': u'Standard',
     u'leather-seat': True,
     u'leather-steering-wheel': u'Optional',
     u'limited-slip-differential': True,
     u'load-bearing-exterior-rack': True,
     u'locking-differential': True,
     u'locking-pickup-truck-tailgate': True,
     u'make': u'GMC',
     u'manual-sunroof': True,
     u'manufactured-in': u'UNITED STATES',
     u'maximum-gvwr': u'6459 lbs',
     u'maximum-payload': u'1462 lbs',
     u'maximum-towing': u'4500 lbs',
     u'model': u'Acadia',
     u'mpg-city': u'16 miles/gallon',
     u'mpg-hwy': u'22 miles/gallon',
     u'msrp': u'$31,765 USD',
     u'navigation-aid': True,
     u'optional-seating': u'7',
     u'overall-height': u'69.90 in.',
     u'overall-length': u'200.70 in.',
     u'overall-width': u'78.20 in.',
     u'passenger-airbag': u'Standard',
     u'passenger-multi-adjustable-power-seat': u'Optional',
     u'passenger-volume': u'cu.ft.',
     u'pickup-truck-bed-liner': True,
     u'pickup-truck-cargo-box-light': True,
     u'power-adjustable-exterior-mirror': u'Standard',
     u'power-door-locks': u'Standard',
     u'power-sliding-side-van-door': True,
     u'power-sunroof': True,
     u'power-trunk-lid': True,
     u'power-windows': u'Standard',
     u'powertrain-warranty-distance': u'100,000 mile',
     u'powertrain-warranty-duration': u'60 month',
     u'rain-sensing-wipers': True,
     u'rear-brake-type': u'Disc',
     u'rear-headroom': u'39.30 in.',
     u'rear-hip-room': u'57.90 in.',
     u'rear-legroom': u'36.90 in.',
     u'rear-shoulder-room': u'61.10 in.',
     u'rear-spoiler': u'Standard',
     u'rear-spring-type': '',
     u'rear-suspension': u'Ind',
     u'rear-window-defogger': u'Standard',
     u'rear-wiper': u'Standard',
     u'remote-ignition': u'Optional',
     u'removable-top': True,
     u'run-flat-tires': True,
     u'running-boards': True,
     u'rust-distance': u'100,000 mile',
     u'rust-duration': u'72 month',
     u'second-row-folding-seat': u'Standard',
     u'second-row-heated-seat': True,
     u'second-row-multi-adjustable-power-seat': True,
     u'second-row-removable-seat': True,
     u'second-row-side-airbag': True,
     u'second-row-side-airbag-with-head-protection': True,
     u'second-row-sound-controls': u'Optional',
     u'separate-driver-front-passenger-climate-controls': u'Optional',
     u'side-head-curtain-airbag': u'Standard',
     u'skid-plate': True,
     u'sliding-rear-pickup-truck-window': True,
     u'splash-guards': True,
     u'standard-gvwr': u'6459 lbs',
     u'standard-payload': u'1462 lbs',
     u'standard-seating': u'8',
     u'standard-towing': u'2000 lbs',
     u'steel-wheels': True,
     u'steering-type': u'R&P',
     u'steering-wheel-mounted-controls': u'Optional',
     u'subwoofer': u'Optional',
     u'tachometer': u'Standard',
     u'tank': u'22.00 gallon',
     u'telematics-system': u'Standard',
     u'telescopic-steering-column': u'Standard',
     u'third-row-removable-seat': True,
     u'tilt-steering': u'Standard',
     u'tilt-steering-column': u'Standard',
     u'tire-pressure-monitor': u'Standard',
     u'tires': u'255/65R18',
     u'tow-hitch-receiver': u'Optional',
     u'towing-preparation-package': u'Optional',
     u'track-front': u'67.10 in.',
     u'track-rear': u'67.10 in.',
     u'traction-control': True,
     u'transmission': u'6-Speed Automatic Overdrive',
     u'trim-level': u'SLE-1 AWD',
     u'trip-computer': True,
     u'trunk-anti-trap-device': True,
     u'turning-diameter': u'40.40 in.',
     u'vehicle-anti-theft': u'Standard',
     u'vehicle-stability-control-system': u'Standard',
     u'vin': u'1GKEV13728J123735',
     u'voice-activated-telephone': u'Standard',
     u'warranty-distance': u'36,000 mile',
     u'warranty-duration': u'36 month',
     u'wheelbase': u'118.90 in.',
     u'width-at-wall': u'in.',
     u'width-at-wheelwell': u'in.',
     u'wind-deflector-for-convertibles': True,
     u'year': u'2008'}


Credits
=======

This project was created and is sponsored by:

.. figure:: http://motion-m.ca/media/img/logo.png
    :figwidth: image

Motion Média (http://motion-m.ca)
