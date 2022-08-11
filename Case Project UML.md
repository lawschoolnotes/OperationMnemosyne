---
title: Case Project UML
created date: 2022-08-11.12:29:37 pm
---

# Case Project UML

## Schema

```plantuml
@startjson
{
    "$schema": "https://json-schema.org/draft-07/schema",
    "id": "/schemas/cases",
    "title": "Case List",
    "description": "Identifiers to find a specific court case",
    "type": "object",
    "properties": {
        "$schema": {
            "type": "string"
        },
        "caseList": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "style": {
                        "description": "Name of the case",
                        "type": "string"
                    },
                    "cite": {
                        "description": "List of parallel cites for the case",
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "vol": {
                                    "type": "integer"
                                },
                                "reporter": {
                                    "type": "string",
                                    "enum": ["U.S.", "S.Ct.", "L.Ed.", "L.Ed.2d", "F.3d"]
                                },
                                "page": {
                                    "type": "integer"
                                }
                            },
                            "required": [
                                "vol",
                                "reporter",
                                "page"
                            ]
                        }
                    },
                    "year": {
                        "type": "integer",
                        "minimum": 1700,
                        "maximum": 2022
                    }
                },
                "required": [
                    "style",
                    "cite",
                    "year"
                ]
        }
    }
}
}
@endjson
```

## Data

```plantuml
@startjson
{
"$schema": "./schemas/cases.schema.json",
"caseList": [
    {
        "style": "44 Liquormart, Inc. v. Rhode Island",
        "cite": [
            {"vol": 517, "reporter": "U.S.", "page": 484}
        ],
        "year": 1996
    },
    {
        "style": "Aaron B. Cooley v. The Board of Wardens of the Port of Philadelphia",
        "cite": [
            {"vol": 53, "reporter": "U.S.", "page": 299}
        ],
        "year": 1851
    },
    {
        "style": "Abbott Laboratories v. Gardner",
        "cite": [
            {"vol": 387, "reporter": "U.S.", "page": 136}
        ],
        "year": 1967
    },
    {
        "style": "Abrams v. United States",
        "cite": [
            {"vol": 250, "reporter": "U.S.", "page": 616}
        ],
        "year": 1919
    },
    {
        "style": "Adderley v. Florida",
        "cite": [
            {"vol": 385, "reporter": "U.S.", "page": 39},
            {"vol": 87, "reporter": "S.Ct.", "page": 242},
            {"vol": 17, "reporter": "L.Ed.2d", "page": 149}
        ],
        "year": 1966
    },
    {
        "style": "Adkins v. Children's Hospital",
        "cite": [
            {"vol": 261, "reporter": "U.S.", "page": 525}
        ],
        "year": 1923
    },
    {
        "style": "A.L.A. Schechter Poultry Corp. v. United States",
        "cite": [
            {"vol": 295, "reporter": "U.S.", "page": 495}
        ],
        "year": 1935
    },
    {
        "style": "Alden v. Maine",
        "cite": [
            {"vol": 527, "reporter": "U.S.", "page": 706}
        ],
        "year": 1999
    },
    {
        "style": "Alexander v. United States",
        "cite": [
            {"vol": 509, "reporter": "U.S.", "page": 544}
        ],
        "year": 1993
    },
    {
        "style": "Allen v. Wright",
        "cite": [
            {"vol": 468, "reporter": "U.S.", "page": 737},
            {"vol": 104, "reporter": "S.Ct.", "page": 3315},
            {"vol": 82, "reporter": "L.Ed.2d", "page": 556}
        ],
        "year": 1984
    },
    {
        "style": "Allgeyer v. Louisiana",
        "cite": [
            {"vol": 165, "reporter": "U.S.", "page": 578}
        ],
        "year": 1897
    },
    {
        "style": "Allied Structural Steel Co. v. Spannaus",
        "cite": [
            {"vol": 438, "reporter": "U.S.", "page": 234},
            {"vol": 98, "reporter": "S.Ct.", "page": 2716},
            {"vol": 57, "reporter": "L.Ed.2d", "page": 727}
        ],
        "year": 1978
    },
    {
        "style": "Amalgamated Food Employees Union Local 590 v. Logan Valley Plaza, Inc.",
        "cite": [
            {"vol": 391, "reporter": "U.S.", "page": 308}
        ],
        "year": 1968
    },
    {
        "style": "Ambach v. Norwick",
        "cite": [
            {"vol": 441, "reporter": "U.S.", "page": 68},
            {"vol": 99, "reporter": "S.Ct.", "page": 1589},
            {"vol": 60, "reporter": "L.Ed.2d", "page": 49}
        ],
        "year": 1979
    },
    {
        "style": "American Civil Liberties Union v. Clapper",
        "cite": [
            {
               "vol": 785,
               "reporter": "F.3d",
               "page": 787,
               "CoA": "2d Cir"
            }
        ],
            "year": 2015
    },
    {
        "style": "American Legion v. American Humanist Association",
        "cite": [
            {"vol": 139, "reporter": "S.Ct.", "page": 2067}
        ],
        "year": 2019
    },
    {
        "style": "Arizona Free Enterprise Club's Freedom Club PAC v. Bennett",
        "cite": [
            {"vol": 564, "reporter": "U.S.", "page": 721},
            {"vol": 131, "reporter": "S.Ct.", "page": 2806},
            {"vol": 180, "reporter": "L.Ed.2d", "page": 664}
        ],
        "year": 2011
    },
    {
        "style": "Arizona v. United States",
        "cite": [
            {"vol": 567, "reporter": "U.S.", "page": 387},
            {"vol": 132, "reporter": "S.Ct.", "page": 2492},
            {"vol": 183, "reporter": "L.Ed.2d", "page": 351}
        ],
        "year": 2012
    },
    {
        "style": "Arkansas Educational Television Commission. v. Forbes",
        "cite": [
            {"vol": 523, "reporter": "U.S.", "page": 666},
            {"vol": 118, "reporter": "S.Ct.", "page": 1633},
            {"vol": 140, "reporter": "L.Ed.2d", "page": 875}
        ],
        "year": 1998
    },
    {
        "style": "Ashcroft v. American Civil Liberties Union (II)",
        "cite": [
            {"vol": 542, "reporter": "U.S.", "page": 656}
        ],
        "year": 2004
    },
    {
        "style": "Ashcroft v. Free Speech Coalition",
        "cite": [
            {"vol": 535, "reporter": "U.S.", "page": 234}
        ],
        "year": 2002
    },
    {
        "style": "Bacchus Imports, Ltd. v. Dias",
        "cite": [
            {"vol": 468, "reporter": "U.S.", "page": 263},
            {"vol": 104, "reporter": "S.Ct.", "page": 3049},
            {"vol": 82, "reporter": "L.Ed.2d", "page": 200}
        ],
        "year": 1984
    },
    {
        "style": "Baker v. Carr",
        "cite": [
            {"vol": 369, "reporter": "U.S.", "page": 186}
        ],
        "year": 1962
    },
    {
        "style": "Baldwin v. Fish & Game Commission of Montana",
        "cite": [
            {"vol": 436, "reporter": "U.S.", "page": 371}
        ],
        "year": 1978
    },
    {
        "style": "Ball v. James",
        "cite": [
            {"vol": 451, "reporter": "U.S.", "page": 355},
            {"vol": 101, "reporter": "S.Ct.", "page": 1811},
            {"vol": 68, "reporter": "L.Ed.2d", "page": 150}
        ],
        "year": 1981
    },
    {
        "style": "Barron v. Mayor & City Council of Baltimore",
        "cite": [
            {"vol": 32, "reporter": "U.S.", "page": 243}
        ],
        "year": 1833
    },
    {
        "style": "Bartnicki v. Vopper",
        "cite": [
            {"vol": 532, "reporter": "U.S.", "page": 514},
            {"vol": 121, "reporter": "S.Ct.", "page": 1753},
            {"vol": 149, "reporter": "L.Ed.2d", "page": 787}
        ],
        "year": 2001
    },
    {
        "style": "Beauharnais v. Illinois",
        "cite": [
            {"vol": 343, "reporter": "U.S.", "page": 250}
        ],
        "year": 1952
    },
    {
        "style": "Bellotti v. Baird",
        "cite": [
            {"vol": 443, "reporter": "U.S.", "page": 622}
        ],
        "year": 1979
    },
    {
        "style": "Bethel School District No. 403 v. Fraser",
        "cite": [
            {"vol": 478, "reporter": "U.S.", "page": 675},
            {"vol": 106, "reporter": "S.Ct.", "page": 3159}
        ],
        "year": 1986
    },
    {
        "style": "Bibb, Director, Dept. of Public Safety of Illinois v. Navajo Freight Lines, Inc.",
        "cite": [
            {"vol": 359, "reporter": "U.S.", "page": 520},
            {"vol": 79, "reporter": "S.Ct.", "page": 962}
        ],
        "year": 1959
    },
    {
        "style": "Blum v. Yaretsky",
        "cite": [
            {"vol": 457, "reporter": "U.S.", "page": 991}
        ],
        "year": 1982
    },
    {
        "style": "BMW of North America, Inc. v. Gore",
        "cite": [
            {"vol": 517, "reporter": "U.S.", "page": 559}
        ],
        "year": 1996
    },
    {
        "style": "Board of Education of Oklahoma City Public Schools v. Dowell",
        "cite": [
            {"vol": 498, "reporter": "U.S.", "page": 237}
        ],
        "year": 1991
    },
    {
        "style": "Board of Regents of State Colleges v. Roth",
        "cite": [
            {"vol": 408, "reporter": "U.S.", "page": 564},
            {"vol": 92, "reporter": "S.Ct.", "page": 2701},
            {"vol": 33, "reporter": "L.Ed.2d", "page": 548}
        ],
        "year": 1972
    },
    {
        "style": "Board of Regents of the University of Wisconsin System v. Southworth",
        "cite": [
            {"vol": 529, "reporter": "U.S.", "page": 217}
        ],
        "year": 2000
    },
    {
        "style": "Boddie v. Connecticut",
        "cite": [
            {"vol": 401, "reporter": "U.S.", "page": 371}
        ],
        "year": 1971
    },
    {
        "style": "Bolger v. Youngs Drug Products Corp.",
        "cite": [
            {"vol": 463, "reporter": "U.S.", "page": 60}
        ],
        "year": 1983
    },
    {
        "style": "Boos v. Barry",
        "cite": [
            {"vol": 485, "reporter": "U.S.", "page": 312}
        ],
        "year": 1988
    },
    {
        "style": "Boumediene v. Bush",
        "cite": [
            {"vol": 553, "reporter": "U.S.", "page": 723}
        ],
        "year": 2008
    },
    {
        "style": "Boy Scouts of America v. Dale",
        "cite": [
            {"vol": 530, "reporter": "U.S.", "page": 640}
        ],
        "year": 2000
    },
    {
        "style": "Brandenburg v. Ohio",
        "cite": [
            {"vol": 395, "reporter": "U.S.", "page": 444}
        ],
        "year": 1969
    },
    {
        "style": "Branzburg v. Hayes",
        "cite": [
            {"vol": 408, "reporter": "U.S.", "page": 665}
        ],
        "year": 1972
    },
    {
        "style": "Brentwood Academy v. Tennessee Secondary School Athletic Assn.",
        "cite": [
            {"vol": 531, "reporter": "U.S.", "page": 288},
            {"vol": 121, "reporter": "S.Ct.", "page": 924},
            {"vol": 148, "reporter": "L.Ed.2d", "page": 807}
        ],
        "year": 2001
    },
    {
        "style": "Brown v. Board of Education (Brown I)",
        "cite": [
            {"vol": 347, "reporter": "U.S.", "page": 483}
        ],
        "year": 1954
    },
    {
        "style": "Brown v. Board of Education (Brown II)",
        "cite": [
            {"vol": 349, "reporter": "U.S.", "page": 249},
            {"vol": 75, "reporter": "S.Ct.", "page": 753},
            {"vol": 99, "reporter": "L.Ed.", "page": 1083}
        ],
        "year": 1955
    },
    {
        "style": "Brown v. Entertainment Merchants Association",
        "cite": [
            {"vol": 564, "reporter": "U.S.", "page": 786},
            {"vol": 131, "reporter": "S.Ct.", "page": 2729}
        ],
        "year": 2011
    },
    {
        "style": "Brown v. Legal Foundation of Washington",
        "cite": [
            {"vol": 538, "reporter": "U.S.", "page": 216}
        ],
        "year": 2003
    },
    {
        "style": "Buckley v. Valeo",
        "cite": [
            {"vol": 424, "reporter": "U.S.", "page": 1}
        ],
        "year": 1976
    },
    {
        "style": "Burton v. Wilmington Parking Authority",
        "cite": [
            {"vol": 365, "reporter": "U.S.", "page": 715}
        ],
        "year": 1961
    },
    {
        "style": "Burwell v. Hobby Lobby Stores, Inc.",
        "cite": [
            {"vol": 573, "reporter": "U.S.", "page": 682}
        ],
        "year": 2014
    },
    {
        "style": "Bush v. Gore",
        "cite": [
            {"vol": 531, "reporter": "U.S.", "page": 98}
        ],
        "year": 2000
    },
    {
        "style": "C & A Carbone, Inc. v. Town of Clarkstown, New York",
        "cite": [
            {"vol": 511, "reporter": "U.S.", "page": 383},
            {"vol": 114, "reporter": "S.Ct.", "page": 1677},
            {"vol": 128, "reporter": "L.Ed.2d", "page": 399}
        ],
        "year": 1994
    },
    {
        "style": "Califano v. Webster",
        "cite": [
            {"vol": 430, "reporter": "U.S.", "page": 313}
        ],
        "year": 1977
    },
    {
        "style": "Carter v. Carter Coal Co.",
        "cite": [
            {"vol": 298, "reporter": "U.S.", "page": 238}
        ],
        "year": 1936
    },
    {
        "style": "Castle Rock v. Gonzales",
        "cite": [
            {"vol": 545, "reporter": "U.S.", "page": 748},
            {"vol": 125, "reporter": "S.Ct.", "page": 2796},
            {"vol": 162, "reporter": "L.Ed.2d", "page": 658}
        ],
        "year": 2005
    },
    {
        "style": "Central Hudson Gas & Electric Corp. v. Public Service Commn. of New York",
        "cite": [
            {"vol": 447, "reporter": "U.S.", "page": 557}
        ],
        "year": 1980
    },
    {
        "style": "Champion v. Ames",
        "cite": [
            {"vol": 188, "reporter": "U.S.", "page": 321}
        ],
        "year": 1903
    },
    {
        "style": "Chaplinsky v. New Hampshire",
        "cite": [
            {"vol": 315, "reporter": "U.S.", "page": 568}
        ],
        "year": 1942
    },
    {
        "style": "Christian Legal Society Chapter of the University of California, Hastings College of the Law v. Martinez",
        "cite": [
            {"vol": 561, "reporter": "U.S.", "page": 661}
        ],
        "year": 2010
    },
    {
        "style": "Church of the Lukumi Babalu Aye, Inc. v. City of Hialeah",
        "cite": [
            {"vol": 508, "reporter": "U.S.", "page": 520}
        ],
        "year": 1993
    },
    {
        "style": "Citizens United v. Federal Election Commission",
        "cite": [
            {"vol": 588, "reporter": "U.S.", "page": 310},
            {"vol": 130, "reporter": "S.Ct.", "page": 876},
            {"vol": 175, "reporter": "L.Ed.2d", "page": 753}
        ],
        "year": 2010
    },
    {
        "style": "City of Boerne v. Flores",
        "cite": [
            {"vol": 521, "reporter": "U.S.", "page": 507},
            {"vol": 117, "reporter": "S.Ct.", "page": 2157}
        ],
        "year": 1997
    },
    {
        "style": "City of Cleburne, Texas v. Cleburne Living Center, Inc.",
        "cite": [
            {"vol": 473, "reporter": "U.S.", "page": 432}
        ],
        "year": 1985
    },
    {
        "style": "City of Erie v. Pap's A.M.",
        "cite": [
            {"vol": 529, "reporter": "U.S.", "page": 277},
            {"vol": 120, "reporter": "S.Ct.", "page": 1382},
            {"vol": 146, "reporter": "L.Ed.2d", "page": 265}
        ],
        "year": 2000
    },
    {
        "style": "City of Littleton, Colorado v. Z.J. Gifts D-4, L.L.C.",
        "cite": [
            {"vol": 514, "reporter": "U.S.", "page": 774}
        ],
        "year": 2004
    },
    {
        "style": "City of Mobile v. Bolden",
        "cite": [
            {"vol": 446, "reporter": "U.S.", "page": 55},
            {"vol": 100, "reporter": "S.Ct.", "page": 1490},
            {"vol": 64, "reporter": "L.Ed.2d", "page": 27}
        ],
        "year": 1980
    },
    {
        "style": "City of Philadelphia v. New Jersey",
        "cite": [
            {"vol": 437, "reporter": "U.S.", "page": 617},
            {"vol": 98, "reporter": "S.Ct.", "page": 2531}
        ],
        "year": 1978
    },
    {
        "style": "City of Renton v. Playtime Theatres, Inc.",
        "cite": [
            {"vol": 475, "reporter": "U.S.", "page": 41}
        ],
        "year": 1986
    },
    {
        "style": "City of Richmond v. J.A. Croson Co.",
        "cite": [
            {"vol": 488, "reporter": "U.S.", "page": 469}
        ],
        "year": 1989
    },
    {
        "style": "Clinton v. City of New York",
        "cite": [
            {"vol": 524, "reporter": "U.S.", "page": 417},
            {"vol": 118, "reporter": "S.Ct.", "page": 2091}
        ],
        "year": 1998
    },
    {
        "style": "Clinton v. Jones",
        "cite": [
            {"vol": 520, "reporter": "U.S.", "page": 681},
            {"vol": 117, "reporter": "S.Ct.", "page": 1636}
        ],
        "year": 1997
    },
    {
        "style": "Cohen v. California",
        "cite": [
            {"vol": 403, "reporter": "U.S.", "page": 15},
            {"vol": 91, "reporter": "S.Ct.", "page": 1780}
        ],
        "year": 1971
    },
    {
        "style": "Cohen v. Cowles Media Co.",
        "cite": [
            {"vol": 501, "reporter": "U.S.", "page": 663}
        ],
        "year": 1991
    },
    {
        "style": "Committee for Public Education & Religious Liberty v. Nyquist, Commissioner of Education of New York",
        "cite": [
            {"vol": 413, "reporter": "U.S.", "page": 756}
        ],
        "year": 1973
    },
    {
        "style": "Coppage v. Kansas",
        "cite": [
            {"vol": 236, "reporter": "U.S.", "page": 1}
        ],
        "year": 1915
    },
    {
        "style": "County of Allegheny v. American Civil Liberties Union, Greater Pittsburgh Chapter",
        "cite": [
            {"vol": 492, "reporter": "U.S.", "page": 573}
        ],
        "year": 1989
    },
    {
        "style": "County of Sacramento v. Lewis",
        "cite": [
            {"vol": 523, "reporter": "U.S.", "page": 833}
        ],
        "year": 1998
    },
    {
        "style": "Cox Broadcasting Corp. v. Cohn",
        "cite": [
            {"vol": 420, "reporter": "U.S.", "page": 469}
        ],
        "year": 1975
    },
    {
        "style": "Craig v. Boren",
        "cite": [
            {"vol": 429, "reporter": "U.S.", "page": 190},
            {"vol": 97, "reporter": "S.Ct.", "page": 451},
            {"vol": 50, "reporter": "L.Ed.2d", "page": 397}
        ],
        "year": 1976
    },
    {
        "style": "Crawford v. Marion County Election Board",
        "cite": [
            {"vol": 553, "reporter": "U.S.", "page": 181}
        ],
        "year": 2008
    },
    {
        "style": "Cruzan v. Director, Missouri Department of Health",
        "cite": [
            {"vol": 497, "reporter": "U.S.", "page": 261},
            {"vol": 110, "reporter": "S.Ct.", "page": 2841}
        ],
        "year": 1990
    },
    {
        "style": "Cutter v. Wilkinson",
        "cite": [
            {"vol": 544, "reporter": "U.S.", "page": 709}
        ],
        "year": 2005
    },
    {
        "style": "Dames & Moore v. Regan, Secretary of the Treasury",
        "cite": [
            {"vol": 453, "reporter": "U.S.", "page": 654}
        ],
        "year": 1981
    },
    {
        "style": "Daniels v. Williams",
        "cite": [
            {"vol": 474, "reporter": "U.S.", "page": 327},
            {"vol": 106, "reporter": "S.Ct.", "page": 662},
            {"vol": 88, "reporter": "L.Ed.2d", "page": 662}
        ],
        "year": 1986
    },
    {
        "style": "Dean Milk Co. v. City of Madison, Wisconsin",
        "cite": [
            {"vol": 340, "reporter": "U.S.", "page": 349},
            {"vol": 71, "reporter": "S.Ct.", "page": 295}
        ],
        "year": 1951
    },
    {
        "style": "Debs v. United States",
        "cite": [
            {"vol": 249, "reporter": "U.S.", "page": 211}
        ],
        "year": 1919
    },
    {
        "style": "Dennis v. United States",
        "cite": [
            {"vol": 341, "reporter": "U.S.", "page": 494}
        ],
        "year": 1951
    },
    {
        "style": "DeShaney v. Winnebago County Dept. of Social Services",
        "cite": [
            {"vol": 489, "reporter": "U.S.", "page": 189}
        ],
        "year": 1989
    },
    {
        "style": "District of Columbia v. Heller",
        "cite": [
            {"vol": 554, "reporter": "U.S.", "page": 570}
        ],
        "year": 2008
    },
    {
        "style": "Dolan v. City of Tigard",
        "cite": [
            {"vol": 512, "reporter": "U.S.", "page": 374},
            {"vol": 114, "reporter": "S.Ct.", "page": 2309},
            {"vol": 129, "reporter": "L.Ed.2d", "page": 304}
        ],
        "year": 1994
    },
    {
        "style": "Dred Scott v. Sandford",
        "cite": [
            {"vol": 60, "reporter": "U.S.", "page": 393}
        ],
        "year": 1857
    },
    {
        "style": "Dun & Bradstreet, Inc. v. Greenmoss Builders, Inc.",
        "cite": [
            {"vol": 472, "reporter": "U.S.", "page": 749},
            {"vol": 105, "reporter": "S.Ct.", "page": 2939},
            {"vol": 86, "reporter": "L.Ed.2d", "page": 593}
        ],
        "year": 1985
    },
    {
        "style": "Duncan v. Louisiana",
        "cite": [
            {"vol": 391, "reporter": "U.S.", "page": 145}
        ],
        "year": 1968
    },
    {
        "style": "Easley v. Cromartie",
        "cite": [
            {"vol": 532, "reporter": "U.S.", "page": 234}
        ],
        "year": 2001
    },
    {
        "style": "Edmonson v. Leesville Concrete Co.",
        "cite": [
            {"vol": 500, "reporter": "U.S.", "page": 614}
        ],
        "year": 1991
    },
    {
        "style": "Eisenstadt v. Baird",
        "cite": [
            {"vol": 405, "reporter": "U.S.", "page": 438}
        ],
        "year": 1972
    },
    {
        "style": "Elk Grove Unified School District v. Newdow",
        "cite": [
            {"vol": 542, "reporter": "U.S.", "page": 1},
            {"vol": 124, "reporter": "S.Ct.", "page": 2301},
            {"vol": 159, "reporter": "L.Ed.2d", "page": 98}
        ],
        "year": 2004
    },
    {
        "style": "Employment Division, Department of Human Resources of Oregon v. Smith",
        "cite": [
            {"vol": 494, "reporter": "U.S.", "page": 872},
            {"vol": 110, "reporter": "S.Ct.", "page": 1595},
            {"vol": 108, "reporter": "L.Ed.2d", "page": 876}
        ],
        "year": 1990
    },
    {
        "style": "Energy Reserves Group, Inc. v. Kansas Power & Light Co.",
        "cite": [
            {"vol": 459, "reporter": "U.S.", "page": 400}
        ],
        "year": 1983
    },
    {
        "style": "Engel v. Vitale",
        "cite": [
            {"vol": 370, "reporter": "U.S.", "page": 421},
            {"vol": 82, "reporter": "S.Ct.", "page": 1261}
        ],
        "year": 1962
    },
    {
        "style": "Evans v. Newton",
        "cite": [
            {"vol": 382, "reporter": "U.S.", "page": 296}
        ],
        "year": 1966
    },
    {
        "style": "Evenwel v. Abbott",
        "cite": [
            {"vol": 136, "reporter": "S.Ct.", "page": 1120}
        ],
        "year": 2016
    },
    {
        "style": "Ex Parte McCardle",
        "cite": [
            {"vol": 74, "reporter": "U.S.", "page": 506},
            {"vol": 19, "reporter": "L.Ed.", "page": 264}
        ],
        "year": 1869
    },
    {
        "style": "Exxon Corp. v. Governor of Maryland",
        "cite": [
            {"vol": 437, "reporter": "U.S.", "page": 117}
        ],
        "year": 1978
    },
    {
        "style": "Federal Communications Commission v. Pacifica Foundation",
        "cite": [
            {"vol": 438, "reporter": "U.S.", "page": 726}
        ],
        "year": 1978
    },
    {
        "style": "Feiner v. New York",
        "cite": [
            {"vol": 340, "reporter": "U.S.", "page": 315},
            {"vol": 71, "reporter": "S.Ct.", "page": 303}
        ],
        "year": 1950
    },
    {
        "style": "First National Bank of Boston v. Bellotti",
        "cite": [
            {"vol": 435, "reporter": "U.S.", "page": 765}
        ],
        "year": 1978
    },
    {
        "style": "Fisher v. University of Texas (Fisher II)",
        "cite": [
            {"vol": 136, "reporter": "S.Ct.", "page": 2198},
            {"vol": 195, "reporter": "L.Ed.2d", "page": 511}
        ],
        "year": 2016
    },
    {
        "style": "Fitzpatrick v. Bitzer",
        "cite": [
            {"vol": 427, "reporter": "U.S.", "page": 445}
        ],
        "year": 1976
    },
    {
        "style": "Flast v. Cohen",
        "cite": [
            {"vol": 392, "reporter": "U.S.", "page": 83},
            {"vol": 88, "reporter": "S.Ct.", "page": 1942},
            {"vol": 20, "reporter": "L.Ed.2d", "page": 947}
        ],
        "year": 1968
    },
    {
        "style": "Florida Lime & Avocado Growers, Inc. v. Paul, Director, Dept. of Agriculture of California",
        "cite": [
            {"vol": 373, "reporter": "U.S.", "page": 132}
        ],
        "year": 1963
    },
    {
        "style": "Florida Star v. B.J.F.",
        "cite": [
            {"vol": 491, "reporter": "U.S.", "page": 524}
        ],
        "year": 1989
    },
    {
        "style": "Foley v. Connelie",
        "cite": [
            {"vol": 435, "reporter": "U.S.", "page": 291}
        ],
        "year": 1978
    },
    {
        "style": "Friedman v. Rogers",
        "cite": [
            {"vol": 440, "reporter": "U.S.", "page": 1}
        ],
        "year": 1979
    },
    {
        "style": "Friends of the Earth, Inc. v. Laidlaw Environmental Services, Inc.",
        "cite": [
            {"vol": 528, "reporter": "U.S.", "page": 167}
        ],
        "year": 2000
    },
    {
        "style": "Frohwerk v. United States",
        "cite": [
            {"vol": 249, "reporter": "U.S.", "page": 204}
        ],
        "year": 1919
    },
    {
        "style": "Frontiero v. Richardson",
        "cite": [
            {"vol": 411, "reporter": "U.S.", "page": 677}
        ],
        "year": 1973
    },
    {
        "style": "Garcetti v. Ceballos",
        "cite": [
            {"vol": 547, "reporter": "U.S.", "page": 410},
            {"vol": 126, "reporter": "S.Ct.", "page": 1951}
        ],
        "year": 2006
    },
    {
        "style": "Garcia v. San Antonio Metropolitan Transit Authority",
        "cite": [
            {"vol": 469, "reporter": "U.S.", "page": 528}
        ],
        "year": 1985
    },
    {
        "style": "Geduldig v. Aiello",
        "cite": [
            {"vol": 417, "reporter": "U.S.", "page": 484}
        ],
        "year": 1974
    },
    {
        "style": "Gertz v. Robert Welch, Inc.",
        "cite": [
            {"vol": 418, "reporter": "U.S.", "page": 323}
        ],
        "year": 1974
    },
    {
        "style": "Gibbons v. Ogden",
        "cite": [
            {"vol": 22, "reporter": "U.S.", "page": 1},
            {"vol": 6, "reporter": "L.Ed.", "page": 23}
        ],
        "year": 1824
    },
    {
        "style": "Gitlow v. New York",
        "cite": [
            {"vol": 268, "reporter": "U.S.", "page": 652}
        ],
        "year": 1925
    },
    {
        "style": "Goldberg v. Kelly",
        "cite": [
            {"vol": 397, "reporter": "U.S.", "page": 254},
            {"vol": 90, "reporter": "S.Ct.", "page": 1011},
            {"vol": 25, "reporter": "L.Ed.2d", "page": 287}
        ],
        "year": 1970
    },
    {
        "style": "Goldwater v. Carter",
        "cite": [
            {"vol": 444, "reporter": "U.S.", "page": 996}
        ],
        "year": 1979
    },
    {
        "style": "Gonzales v. Carhart",
        "cite": [
            {"vol": 550, "reporter": "U.S.", "page": 124},
            {"vol": 127, "reporter": "S.Ct.", "page": 1610},
            {"vol": 167, "reporter": "L.Ed.2d", "page": 480}
        ],
        "year": 2007
    },
    {
        "style": "Gonzales v. Raich",
        "cite": [
            {"vol": 545, "reporter": "U.S.", "page": 1}
        ],
        "year": 2005
    },
    {
        "style": "Gooding v. Wilson",
        "cite": [
            {"vol": 405, "reporter": "U.S.", "page": 518}
        ],
        "year": 1972
    },
    {
        "style": "Goss v. Lopez",
        "cite": [
            {"vol": 419, "reporter": "U.S.", "page": 565}
        ],
        "year": 1975
    },
    {
        "style": "Graham v. Richardson",
        "cite": [
            {"vol": 403, "reporter": "U.S.", "page": 365},
            {"vol": 91, "reporter": "S.Ct.", "page": 1848},
            {"vol": 29, "reporter": "L.Ed.2d", "page": 534}
        ],
        "year": 1971
    },
    {
        "style": "Gratz v. Bollinger",
        "cite": [
            {"vol": 539, "reporter": "U.S.", "page": 244}
        ],
        "year": 2003
    },
    {
        "style": "Greer v. Spock",
        "cite": [
            {"vol": 424, "reporter": "U.S.", "page": 828}
        ],
        "year": 1976
    },
    {
        "style": "Griswold v. Connecticut",
        "cite": [
            {"vol": 381, "reporter": "U.S.", "page": 479}
        ],
        "year": 1965
    },
    {
        "style": "Grutter v. Bollinger",
        "cite": [
            {"vol": 539, "reporter": "U.S.", "page": 306}
        ],
        "year": 2003
    },
    {
        "style": "Hague v. Committee for Industrial Organization",
        "cite": [
            {"vol": 307, "reporter": "U.S.", "page": 496}
        ],
        "year": 1939
    },
    {
        "style": "Hamdi v. Rumsfeld",
        "cite": [
            {"vol": 542, "reporter": "U.S.", "page": 507},
            {"vol": 124, "reporter": "S.Ct.", "page": 2633}
        ],
        "year": 2004
    },
    {
        "style": "Hammer v. Dagenhart",
        "cite": [
            {"vol": 247, "reporter": "U.S.", "page": 251},
            {"vol": 38, "reporter": "S.Ct.", "page": 529}
        ],
        "year": 1918
    },
    {
        "style": "Harper v. Virginia State Board of Elections",
        "cite": [
            {"vol": 383, "reporter": "U.S.", "page": 663},
            {"vol": 86, "reporter": "S.Ct.", "page": 1079}
        ],
        "year": 1966
    },
    {
        "style": "Hawaii Housing Authority v. Midkiff",
        "cite": [
            {"vol": 467, "reporter": "U.S.", "page": 229}
        ],
        "year": 1984
    },
    {
        "style": "Hazelwood School District v. Kuhlmeier",
        "cite": [
            {"vol": 484, "reporter": "U.S.", "page": 260},
            {"vol": 108, "reporter": "S.Ct.", "page": 562},
            {"vol": 98, "reporter": "L.Ed.2d", "page": 592}
        ],
        "year": 1988
    },
    {
        "style": "Heart of Atlanta Motel, Inc. v. United States",
        "cite": [
            {"vol": 379, "reporter": "U.S.", "page": 241}
        ],
        "year": 1964
    },
    {
        "style": "Hein v. Freedom From Religion Foundation",
        "cite": [
            {"vol": 551, "reporter": "U.S.", "page": 587}
        ],
        "year": 2007
    },
    {
        "style": "Hill v. Colorado",
        "cite": [
            {"vol": 530, "reporter": "U.S.", "page": 703}
        ],
        "year": 2000
    },
    {
        "style": "Hines, Secretary of Labor & Industry of Pennsylvania v. Davidowitz",
        "cite": [
            {"vol": 312, "reporter": "U.S.", "page": 52}
        ],
        "year": 1941
    },
    {
        "style": "Holder v. Humanitarian Law Project",
        "cite": [
            {"vol": 561, "reporter": "U.S.", "page": 1},
            {"vol": 130, "reporter": "S.Ct.", "page": 2705}
        ],
        "year": 2010
    },
    {
        "style": "Hollingsworth v. Perry",
        "cite": [
            {"vol": 570, "reporter": "U.S.", "page": 693},
            {"vol": 133, "reporter": "S.Ct.", "page": 2652},
            {"vol": 186, "reporter": "L.Ed.2d", "page": 768}
        ],
        "year": 2013
    },
    {
        "style": "Home Building & Loan Assn. v. Blaisdell",
        "cite": [
            {"vol": 290, "reporter": "U.S.", "page": 398}
        ],
        "year": 1934
    },
    {
        "style": "Houchins v. KQED",
        "cite": [
            {"vol": 438, "reporter": "U.S.", "page": 1}
        ],
        "year": 1978
    },
    {
        "style": "Houston, East & West Texas Railway Co. v. United States (The Shreveport Rate Cases)",
        "cite": [
            {"vol": 234, "reporter": "U.S.", "page": 342}
        ],
        "year": 1914
    },
    {
        "style": "H.P. Hood & Sons, Inc. v. Du Mond, Commissioner of Agriculture & Markets of New York",
        "cite": [
            {"vol": 336, "reporter": "U.S.", "page": 525},
            {"vol": 69, "reporter": "S.Ct.", "page": 657},
            {"vol": 93, "reporter": "L.Ed.", "page": 865}
        ],
        "year": 1949
    },
    {
        "style": "Hudgens v. National Labor Relations Board",
        "cite": [
            {"vol": 424, "reporter": "U.S.", "page": 507}
        ],
        "year": 1976
    },
    {
        "style": "Hughes v. Oklahoma",
        "cite": [
            {"vol": 441, "reporter": "U.S.", "page": 322},
            {"vol": 99, "reporter": "S.Ct.", "page": 1727},
            {"vol": 60, "reporter": "L.Ed.2d", "page": 250}
        ],
        "year": 1979
    },
    {
        "style": "Hunt, Governor of the State of North Carolina v. Washington State Apple Advertising Commn.",
        "cite": [
            {"vol": 432, "reporter": "U.S.", "page": 333},
            {"vol": 97, "reporter": "S.Ct.", "page": 2434}
        ],
        "year": 1977
    },
    {
        "style": "Hurley v. Irish-American Gay, Lesbian, & Bisexual Group of Boston",
        "cite": [
            {"vol": 515, "reporter": "U.S.", "page": 557}
        ],
        "year": 1995
    },
    {
        "style": "Hustler Magazine v. Falwell",
        "cite": [
            {"vol": 485, "reporter": "U.S.", "page": 46},
            {"vol": 108, "reporter": "S.Ct.", "page": 876}
        ],
        "year": 1988
    },
    {
        "style": "Immigration and Naturalization Service v. Chadha",
        "cite": [
            {"vol": 462, "reporter": "U.S.", "page": 919},
            {"vol": 103, "reporter": "S.Ct.", "page": 2764}
        ],
        "year": 1983
    },
    {
        "style": "International Society for Krishna Consciousness, Inc. v. Lee",
        "cite": [
            {"vol": 505, "reporter": "U.S.", "page": 672},
            {"vol": 112, "reporter": "S.Ct.", "page": 2701}
        ],
        "year": 1992
    },
    {
        "style": "Jackson v. Metropolitan Edison Co.",
        "cite": [
            {"vol": 419, "reporter": "U.S.", "page": 345}
        ],
        "year": 1974
    },
    {
        "style": "Johnson v. California",
        "cite": [
            {"vol": 543, "reporter": "U.S.", "page": 499}
        ],
        "year": 2005
    },
    {
        "style": "Kassel v. Consolidated Freightways Corp.",
        "cite": [
            {"vol": 450, "reporter": "U.S.", "page": 662},
            {"vol": 101, "reporter": "S.Ct.", "page": 1309},
            {"vol": 67, "reporter": "L.Ed.2d", "page": 580}
        ],
        "year": 1981
    },
    {
        "style": "Katzenbach v. McClung",
        "cite": [
            {"vol": 379, "reporter": "U.S.", "page": 294}
        ],
        "year": 1964
    },
    {
        "style": "Katzenbach v. Morgan",
        "cite": [
            {"vol": 384, "reporter": "U.S.", "page": 641}
        ],
        "year": 1966
    },
    {
        "style": "Kelo v. City of New London",
        "cite": [
            {"vol": 125, "reporter": "S.Ct.", "page": 2655},
            {"vol": 545, "reporter": "U.S.", "page": 469}
        ],
        "year": 2005
    },
    {
        "style": "Korematsu v. United States",
        "cite": [
            {"vol": 323, "reporter": "U.S.", "page": 214}
        ],
        "year": 1944
    },
    {
        "style": "Kramer v. Union Free School District",
        "cite": [
            {"vol": 395, "reporter": "U.S.", "page": 621}
        ],
        "year": 1969
    },
    {
        "style": "Larson v. Valente",
        "cite": [
            {"vol": 456, "reporter": "U.S.", "page": 228}
        ],
        "year": 1982
    },
    {
        "style": "Lawrence v. Texas",
        "cite": [
            {"vol": 539, "reporter": "U.S.", "page": 558}
        ],
        "year": 2003
    },
    {
        "style": "Lee v. Weisman",
        "cite": [
            {"vol": 505, "reporter": "U.S.", "page": 577}
        ],
        "year": 1992
    },
    {
        "style": "Legal Services Corp. v. Velazquez",
        "cite": [
            {"vol": 531, "reporter": "U.S.", "page": 533}
        ],
        "year": 2001
    },
    {
        "style": "Lehman v. City of Shaker Heights",
        "cite": [
            {"vol": 418, "reporter": "U.S.", "page": 298}
        ],
        "year": 1974
    },
    {
        "style": "Lemon v. Kurtzman",
        "cite": [
            {"vol": 403, "reporter": "U.S.", "page": 602}
        ],
        "year": 1971
    },
    {
        "style": "Lewis v. Casey",
        "cite": [
            {"vol": 518, "reporter": "U.S.", "page": 343}
        ],
        "year": 1996
    },
    {
        "style": "Linmark Associates, Inc. v. Township of Willingboro",
        "cite": [
            {"vol": 431, "reporter": "U.S.", "page": 85}
        ],
        "year": 1977
    },
    {
        "style": "Lloyd Corp. v. Tanner",
        "cite": [
            {"vol": 407, "reporter": "U.S.", "page": 551}
        ],
        "year": 1972
    },
    {
        "style": "Lochner v. New York",
        "cite": [
            {"vol": 198, "reporter": "U.S.", "page": 45}
        ],
        "year": 1905
    },
    {
        "style": "Locke v. Davey",
        "cite": [
            {"vol": 540, "reporter": "U.S.", "page": 714}
        ],
        "year": 2004
    },
    {
        "style": "Loretto v. Teleprompter Manhattan CATV Corp.",
        "cite": [
            {"vol": 458, "reporter": "U.S.", "page": 419}
        ],
        "year": 1982
    },
    {
        "style": "Lorillard Tobacco Co. v. Reilly",
        "cite": [
            {"vol": 533, "reporter": "U.S.", "page": 525}
        ],
        "year": 2001
    },
    {
        "style": "Loving v. Virginia",
        "cite": [
            {"vol": 388, "reporter": "U.S.", "page": 1}
        ],
        "year": 1967
    },
    {
        "style": "Lucas v. South Carolina Coastal Council",
        "cite": [
            {"vol": 505, "reporter": "U.S.", "page": 1003}
        ],
        "year": 1992
    },
    {
        "style": "Lugar v. Edmondson Oil Co.",
        "cite": [
            {"vol": 457, "reporter": "U.S.", "page": 922},
            {"vol": 102, "reporter": "S.Ct.", "page": 2744},
            {"vol": 73, "reporter": "L.Ed.2d", "page": 482}
        ],
        "year": 1982
    },
    {
        "style": "Maher v. Roe",
        "cite": [
            {"vol": 432, "reporter": "U.S.", "page": 464}
        ],
        "year": 1977
    },
    {
        "style": "Maine v. Taylor & United States",
        "cite": [
            {"vol": 477, "reporter": "U.S.", "page": 131}
        ],
        "year": 1986
    },
    {
        "style": "Manhattan Community Access Corp. v. Halleck",
        "cite": [
            {"vol": 139, "reporter": "S.Ct.", "page": 1921}
        ],
        "year": 2019
    },
    {
        "style": "Marbury v. Madison",
        "cite": [
            {"vol": 5, "reporter": "U.S.", "page": 137},
            {"vol": 2, "reporter": "L.Ed.", "page": 60}
        ],
        "year": 1803
    },
    {
        "style": "Marsh v. Alabama",
        "cite": [
            {"vol": 326, "reporter": "U.S.", "page": 501}
        ],
        "year": 1946
    },
    {
        "style": "Massachusetts Board of Retirement v. Murgia",
        "cite": [
            {"vol": 427, "reporter": "U.S.", "page": 307}
        ],
        "year": 1976
    },
    {
        "style": "Massachusetts v. Environmental Protection Agency",
        "cite": [
            {"vol": 549, "reporter": "U.S.", "page": 497}
        ],
        "year": 2007
    },
    {
        "style": "Mathews v. Eldridge",
        "cite": [
            {"vol": 424, "reporter": "U.S.", "page": 319}
        ],
        "year": 1975
    },
    {
        "style": "McCleskey v. Kemp",
        "cite": [
            {"vol": 481, "reporter": "U.S.", "page": 279}
        ],
        "year": 1987
    },
    {
        "style": "McCreary County v. American Civil Liberties Union of Kentucky",
        "cite": [
            {"vol": 545, "reporter": "U.S.", "page": 844}
        ],
        "year": 2005
    },
    {
        "style": "McCulloch v. Maryland",
        "cite": [
            {"vol": 4, "reporter": "L.Ed.", "page": 579},
            {"vol": 17, "reporter": "U.S.", "page": 316}
        ],
        "year": 1819
    },
    {
        "style": "McDonald v. City of Chicago",
        "cite": [
            {"vol": 561, "reporter": "U.S.", "page": 742}
        ],
        "year": 2010
    },
    {
        "style": "McIntyre v. Ohio Elections Commission",
        "cite": [
            {"vol": 514, "reporter": "U.S.", "page": 334}
        ],
        "year": 1995
    },
    {
        "style": "Meyer v. Nebraska",
        "cite": [
            {"vol": 262, "reporter": "U.S.", "page": 390}
        ],
        "year": 1923
    },
    {
        "style": "Miami Herald v. Tornillo",
        "cite": [
            {"vol": 418, "reporter": "U.S.", "page": 241}
        ],
        "year": 1974
    },
    {
        "style": "Michael H. v. Gerald D.",
        "cite": [
            {"vol": 491, "reporter": "U.S.", "page": 110}
        ],
        "year": 1989
    },
    {
        "style": "Michael M. v. Superior Court of Sonoma County",
        "cite": [
            {"vol": 450, "reporter": "U.S.", "page": 464},
            {"vol": 101, "reporter": "S.Ct.", "page": 1200},
            {"vol": 67, "reporter": "L.Ed.2d", "page": 437}
        ],
        "year": 1981
    },
    {
        "style": "Miller v. California",
        "cite": [
            {"vol": 413, "reporter": "U.S.", "page": 15}
        ],
        "year": 1973
    },
    {
        "style": "Miller v. Schoene",
        "cite": [
            {"vol": 276, "reporter": "U.S.", "page": 272}
        ],
        "year": 1928
    },
    {
        "style": "Milliken v. Bradley",
        "cite": [
            {"vol": 418, "reporter": "U.S.", "page": 717}
        ],
        "year": 1974
    },
    {
        "style": "Minneapolis Star & Tribune Co. v. Minnesota Commissioner of Revenue",
        "cite": [
            {"vol": 460, "reporter": "U.S.", "page": 575},
            {"vol": 103, "reporter": "S.Ct.", "page": 1365},
            {"vol": 75, "reporter": "L.Ed.2d", "page": 295}
        ],
        "year": 1983
    },
    {
        "style": "Mississippi University for Women v. Hogan",
        "cite": [
            {"vol": 458, "reporter": "U.S.", "page": 718},
            {"vol": 102, "reporter": "S.Ct.", "page": 3331},
            {"vol": 73, "reporter": "L.Ed.2d", "page": 1090}
        ],
        "year": 1982
    },
    {
        "style": "Mitchell v. Helms",
        "cite": [
            {"vol": 530, "reporter": "U.S.", "page": 793},
            {"vol": 120, "reporter": "S.Ct.", "page": 2530},
            {"vol": 147, "reporter": "L.Ed.2d", "page": 660}
        ],
        "year": 2000
    },
    {
        "style": "M.L.B. v. S.L.J.",
        "cite": [
            {"vol": 519, "reporter": "U.S.", "page": 102}
        ],
        "year": 1996
    },
    {
        "style": "Moore v. City of East Cleveland, Ohio",
        "cite": [
            {"vol": 431, "reporter": "U.S.", "page": 494}
        ],
        "year": 1977
    },
    {
        "style": "Moose Lodge No. 107 v. Irvis",
        "cite": [
            {"vol": 407, "reporter": "U.S.", "page": 163},
            {"vol": 92, "reporter": "S.Ct.", "page": 1965},
            {"vol": 32, "reporter": "L.Ed.2d", "page": 627}
        ],
        "year": 1972
    },
    {
        "style": "Morrison v. Olson",
        "cite": [
            {"vol": 487, "reporter": "U.S.", "page": 654},
            {"vol": 108, "reporter": "S.Ct.", "page": 2597},
            {"vol": 101, "reporter": "L.Ed.2d", "page": 569}
        ],
        "year": 1988
    },
    {
        "style": "Morse v. Frederick",
        "cite": [
            {"vol": 551, "reporter": "U.S.", "page": 393},
            {"vol": 127, "reporter": "S.Ct.", "page": 2618},
            {"vol": 168, "reporter": "L.Ed.2d", "page": 290}
        ],
        "year": 2007
    },
    {
        "style": "Muller v. Oregon",
        "cite": [
            {"vol": 208, "reporter": "U.S.", "page": 412},
            {"vol": 28, "reporter": "S.Ct.", "page": 324},
            {"vol": 52, "reporter": "L.Ed.", "page": 551}
        ],
        "year": 1907
    },
    {
        "style": "NAACP v. State of Alabama ex rel. Patterson",
        "cite": [
            {"vol": 357, "reporter": "U.S.", "page": 449}
        ],
        "year": 1958
    },
    {
        "style": "National Endowment for the Arts v. Finley",
        "cite": [
            {"vol": 524, "reporter": "U.S.", "page": 569},
            {"vol": 118, "reporter": "S.Ct.", "page": 2168},
            {"vol": 141, "reporter": "L.Ed.2d", "page": 500}
        ],
        "year": 1998
    },
    {
        "style": "National Federation of Independent Business v. Sebelius",
        "cite": [
            {"vol": 132, "reporter": "S.Ct.", "page": 2566},
            {"vol": 567, "reporter": "U.S.", "page": 519}
        ],
        "year": 2012
    },
    {
        "style": "National Labor Relations Board v. Jones & Laughlin Steel Corp.",
        "cite": [
            {"vol": 301, "reporter": "U.S.", "page": 1}
        ],
        "year": 1937
    },
    {
        "style": "National League of Cities v. Usery",
        "cite": [
            {"vol": 426, "reporter": "U.S.", "page": 833}
        ],
        "year": 1976
    },
    {
        "style": "Near v. State of Minnesota ex rel. Olson",
        "cite": [
            {"vol": 283, "reporter": "U.S.", "page": 697},
            {"vol": 51, "reporter": "S.Ct.", "page": 625},
            {"vol": 75, "reporter": "L.Ed.", "page": 1357}
        ],
        "year": 1931
    },
    {
        "style": "Nebbia v. New York",
        "cite": [
            {"vol": 291, "reporter": "U.S.", "page": 502}
        ],
        "year": 1934
    },
    {
        "style": "Nebraska Press Assn. v. Stuart",
        "cite": [
            {"vol": 427, "reporter": "U.S.", "page": 539},
            {"vol": 96, "reporter": "S.Ct.", "page": 2791},
            {"vol": 49, "reporter": "L.Ed.2d", "page": 683}
        ],
        "year": 1976
    },
    {
        "style": "New York City Transit Authority v. Beazer",
        "cite": [
            {"vol": 440, "reporter": "U.S.", "page": 568}
        ],
        "year": 1979
    },
    {
        "style": "New York Times Co. v. Sullivan",
        "cite": [
            {"vol": 376, "reporter": "U.S.", "page": 254}
        ],
        "year": 1964
    },
    {
        "style": "New York Times Co. v. United States",
        "cite": [
            {"vol": 403, "reporter": "U.S.", "page": 713},
            {"vol": 91, "reporter": "S.Ct.", "page": 2140},
            {"vol": 29, "reporter": "L.Ed.2d", "page": 822}
        ],
        "year": 1971
    },
    {
        "style": "New York v. Ferber",
        "cite": [
            {"vol": 458, "reporter": "U.S.", "page": 747},
            {"vol": 102, "reporter": "S.Ct.", "page": 3348}
        ],
        "year": 1982
    },
    {
        "style": "New York v. United States",
        "cite": [
            {"vol": 505, "reporter": "U.S.", "page": 144},
            {"vol": 112, "reporter": "S.Ct.", "page": 2408}
        ],
        "year": 1992
    },
    {
        "style": "Nguyen v. Immigration and Naturalization Service",
        "cite": [
            {"vol": 533, "reporter": "U.S.", "page": 53}
        ],
        "year": 2001
    },
    {
        "style": "Nixon v. Shrink Missouri Government PAC",
        "cite": [
            {"vol": 528, "reporter": "U.S.", "page": 377}
        ],
        "year": 2000
    },
    {
        "style": "Nixon v. United States",
        "cite": [
            {"vol": 506, "reporter": "U.S.", "page": 224},
            {"vol": 113, "reporter": "S.Ct.", "page": 732}
        ],
        "year": 1993
    },
    {
        "style": "Norwood v. Harrison",
        "cite": [
            {"vol": 413, "reporter": "U.S.", "page": 455}
        ],
        "year": 1973
    },
    {
        "style": "Obergefell v. Hodges",
        "cite": [
            {"vol": 135, "reporter": "S.Ct.", "page": 1039},
            {"vol": 576, "reporter": "U.S.", "page": 644}
        ],
        "year": 2015
    },
    {
        "style": "Orr v. Orr",
        "cite": [
            {"vol": 440, "reporter": "U.S.", "page": 268}
        ],
        "year": 1979
    },
    {
        "style": "Pacific Gas & Electric Co. v. State Energy Resources Conservation & Development Commission",
        "cite": [
            {"vol": 461, "reporter": "U.S.", "page": 190}
        ],
        "year": 1983
    },
    {
        "style": "Palazzolo v. Rhode Island",
        "cite": [
            {"vol": 533, "reporter": "U.S.", "page": 606}
        ],
        "year": 2001
    },
    {
        "style": "Palmer v. Thompson",
        "cite": [
            {"vol": 403, "reporter": "U.S.", "page": 217}
        ],
        "year": 1971
    },
    {
        "style": "Palmore v. Sidoti",
        "cite": [
            {"vol": 466, "reporter": "U.S.", "page": 429},
            {"vol": 104, "reporter": "S.Ct.", "page": 1879},
            {"vol": 80, "reporter": "L.Ed.2d", "page": 421}
        ],
        "year": 1984
    },
    {
        "style": "Panama Refining Co. v. Ryan",
        "cite": [
            {"vol": 293, "reporter": "U.S.", "page": 388},
            {"vol": 55, "reporter": "S.Ct.", "page": 241},
            {"vol": 79, "reporter": "L.Ed.", "page": 446}
        ],
        "year": 1935
    },
    {
        "style": "Parents Involved in Community Schools v. Seattle School Dist. No. 1",
        "cite": [
            {"vol": 551, "reporter": "U.S.", "page": 701},
            {"vol": 127, "reporter": "S.Ct.", "page": 2738},
            {"vol": 168, "reporter": "L.Ed.2d", "page": 508}
        ],
        "year": 2007
    },
    {
        "style": "Paris Adult Theatre I v. Slaton",
        "cite": [
            {"vol": 413, "reporter": "U.S.", "page": 49},
            {"vol": 93, "reporter": "S.Ct.", "page": 2628}
        ],
        "year": 1973
    },
    {
        "style": "Parker v. Levy",
        "cite": [
            {"vol": 417, "reporter": "U.S.", "page": 733}
        ],
        "year": 1974
    },
    {
        "style": "Paul v. Davis",
        "cite": [
            {"vol": 424, "reporter": "U.S.", "page": 693}
        ],
        "year": 1976
    },
    {
        "style": "Pell v. Procunier",
        "cite": [
            {"vol": 417, "reporter": "U.S.", "page": 817}
        ],
        "year": 1974
    },
    {
        "style": "Penn Central Transportation Co. v. New York City",
        "cite": [
            {"vol": 438, "reporter": "U.S.", "page": 104},
            {"vol": 98, "reporter": "S.Ct.", "page": 2848},
            {"vol": 57, "reporter": "L.Ed.2d", "page": 631}
        ],
        "year": 1978
    },
    {
        "style": "Pennsylvania Coal Co. v. Mahon",
        "cite": [
            {"vol": 260, "reporter": "U.S.", "page": 393}
        ],
        "year": 1922
    },
    {
        "style": "Perry Education Assn. v. Perry Local Educators' Assn.",
        "cite": [
            {"vol": 460, "reporter": "U.S.", "page": 37},
            {"vol": 103, "reporter": "S.Ct.", "page": 948}
        ],
        "year": 1983
    },
    {
        "style": "Personnel Administrator of Massachusetts v. Feeney",
        "cite": [
            {"vol": 442, "reporter": "U.S.", "page": 156},
            {"vol": 99, "reporter": "S.Ct.", "page": 2282},
            {"vol": 60, "reporter": "L.Ed.2d", "page": 870}
        ],
        "year": 1979
    },
    {
        "style": "Philip Morris USA v. Williams",
        "cite": [
            {"vol": 549, "reporter": "U.S.", "page": 346}
        ],
        "year": 2007
    },
    {
        "style": "Pierce County, Washington v. Guillen",
        "cite": [
            {"vol": 537, "reporter": "U.S.", "page": 129}
        ],
        "year": 2003
    },
    {
        "style": "Pike v. Bruce Church, Inc.",
        "cite": [
            {"vol": 397, "reporter": "U.S.", "page": 137}
        ],
        "year": 1970
    },
    {
        "style": "Planned Parenthood v. Casey",
        "cite": [
            {"vol": 505, "reporter": "U.S.", "page": 833}
        ],
        "year": 1992
    },
    {
        "style": "Plaut v. Spendthrift Farm, Inc.",
        "cite": [
            {"vol": 514, "reporter": "U.S.", "page": 211}
        ],
        "year": 1995
    },
    {
        "style": "Pleasant Grove City, Utah v. Summum",
        "cite": [
            {"vol": 555, "reporter": "U.S.", "page": 460}
        ],
        "year": 2009
    },
    {
        "style": "Plessy v. Ferguson",
        "cite": [
            {"vol": 163, "reporter": "U.S.", "page": 537}
        ],
        "year": 1896
    },
    {
        "style": "Plyler v. Doe",
        "cite": [
            {"vol": 457, "reporter": "U.S.", "page": 202},
            {"vol": 102, "reporter": "S.Ct.", "page": 2382},
            {"vol": 72, "reporter": "L.Ed.2d", "page": 786}
        ],
        "year": 1982
    },
    {
        "style": "Poe v. Ullman",
        "cite": [
            {"vol": 367, "reporter": "U.S.", "page": 497}
        ],
        "year": 1961
    },
    {
        "style": "Police Department of the City of Chicago v. Mosley",
        "cite": [
            {"vol": 408, "reporter": "U.S.", "page": 92}
        ],
        "year": 1972
    },
    {
        "style": "Powell v. McCormack",
        "cite": [
            {"vol": 395, "reporter": "U.S.", "page": 486},
            {"vol": 89, "reporter": "S.Ct.", "page": 1944}
        ],
        "year": 1969
    },
    {
        "style": "Printz v. United States",
        "cite": [
            {"vol": 521, "reporter": "U.S.", "page": 898}
        ],
        "year": 1997
    },
    {
        "style": "Railway Express Agency, Inc. v. New York",
        "cite": [
            {"vol": 336, "reporter": "U.S.", "page": 106}
        ],
        "year": 1949
    },
    {
        "style": "Randall v. Sorrell",
        "cite": [
            {"vol": 548, "reporter": "U.S.", "page": 230}
        ],
        "year": 2006
    },
    {
        "style": "R.A.V. v. City of St. Paul, Minnesota",
        "cite": [
            {"vol": 505, "reporter": "U.S.", "page": 377},
            {"vol": 112, "reporter": "S.Ct.", "page": 2538},
            {"vol": 120, "reporter": "L.Ed.2d", "page": 305}
        ],
        "year": 1992
    },
    {
        "style": "Red Lion Broadcasting Co. v. Federal Communications Commn.",
        "cite": [
            {"vol": 395, "reporter": "U.S.", "page": 367}
        ],
        "year": 1969
    },
    {
        "style": "Reed v. Town of Gilbert",
        "cite": [
            {"vol": 576, "reporter": "U.S.", "page": 155},
            {"vol": 135, "reporter": "S.Ct.", "page": 2218}
        ],
        "year": 2015
    },
    {
        "style": "Reeves, Inc. v. Stake",
        "cite": [
            {"vol": 447, "reporter": "U.S.", "page": 429},
            {"vol": 100, "reporter": "S.Ct.", "page": 2271},
            {"vol": 65, "reporter": "L.Ed.2d", "page": 244}
        ],
        "year": 1980
    },
    {
        "style": "Reitman v. Mulkey",
        "cite": [
            {"vol": 387, "reporter": "U.S.", "page": 369}
        ],
        "year": 1967
    },
    {
        "style": "Rendell-Baker v. Kohn",
        "cite": [
            {"vol": 457, "reporter": "U.S.", "page": 830},
            {"vol": 102, "reporter": "S.Ct.", "page": 2764},
            {"vol": 73, "reporter": "L.Ed.2d", "page": 418}
        ],
        "year": 1982
    },
    {
        "style": "Reno v. American Civil Liberties Union",
        "cite": [
            {"vol": 521, "reporter": "U.S.", "page": 844}
        ],
        "year": 1997
    },
    {
        "style": "Reno v. Condon",
        "cite": [
            {"vol": 528, "reporter": "U.S.", "page": 141}
        ],
        "year": 2000
    },
    {
        "style": "Republican Party of Minnesota v. White",
        "cite": [
            {"vol": 536, "reporter": "U.S.", "page": 765}
        ],
        "year": 2002
    },
    {
        "style": "Reynolds v. Sims",
        "cite": [
            {"vol": 377, "reporter": "U.S.", "page": 533},
            {"vol": 84, "reporter": "S.Ct.", "page": 1362}
        ],
        "year": 1964
    },
    {
        "style": "Richard Nixon v. A. Ernest Fitzgerald",
        "cite": [
            {"vol": 457, "reporter": "U.S.", "page": 731},
            {"vol": 102, "reporter": "S.Ct.", "page": 2690}
        ],
        "year": 1982
    },
    {
        "style": "Richmond Newspapers v. Virginia",
        "cite": [
            {"vol": 448, "reporter": "U.S.", "page": 555}
        ],
        "year": 1980
    },
    {
        "style": "Roberts v. United States Jaycees",
        "cite": [
            {"vol": 468, "reporter": "U.S.", "page": 609}
        ],
        "year": 1984
    },
    {
        "style": "Roe v. Wade",
        "cite": [
            {"vol": 410, "reporter": "U.S.", "page": 113},
            {"vol": 93, "reporter": "S.Ct.", "page": 705},
            {"vol": 35, "reporter": "L.Ed.2d", "page": 147}
        ],
        "year": 1973
    },
    {
        "style": "Romer v. Evans",
        "cite": [
            {"vol": 517, "reporter": "U.S.", "page": 620}
        ],
        "year": 1996
    },
    {
        "style": "Rosenberger v. Rector & Visitors of the University of Virginia",
        "cite": [
            {"vol": 515, "reporter": "U.S.", "page": 819}
        ],
        "year": 1995
    },
    {
        "style": "Rostker v. Goldberg",
        "cite": [
            {"vol": 453, "reporter": "U.S.", "page": 57},
            {"vol": 101, "reporter": "S.Ct.", "page": 2646},
            {"vol": 69, "reporter": "L.Ed.2d", "page": 478}
        ],
        "year": 1981
    },
    {
        "style": "Roth v. United States",
        "cite": [
            {"vol": 354, "reporter": "U.S.", "page": 476}
        ],
        "year": 1957
    },
    {
        "style": "Rumsfeld v. Forum for Academic & Institutional Rights, Inc.",
        "cite": [
            {"vol": 547, "reporter": "U.S.", "page": 47},
            {"vol": 126, "reporter": "S.Ct.", "page": 1297},
            {"vol": 164, "reporter": "L.Ed.2d", "page": 156}
        ],
        "year": 2006
    },
    {
        "style": "Rust v. Sullivan",
        "cite": [
            {"vol": 500, "reporter": "U.S.", "page": 173},
            {"vol": 111, "reporter": "S.Ct.", "page": 1759}
        ],
        "year": 1991
    },
    {
        "style": "Sable Communications of California, Inc. v. Federal Communications Commn.",
        "cite": [
            {"vol": 492, "reporter": "U.S.", "page": 115},
            {"vol": 109, "reporter": "S.Ct.", "page": 2829},
            {"vol": 106, "reporter": "L.Ed.2d", "page": 93}
        ],
        "year": 1989
    },
    {
        "style": "Sabri v. United States",
        "cite": [
            {"vol": 541, "reporter": "U.S.", "page": 600}
        ],
        "year": 2004
    },
    {
        "style": "Saenz v. Roe",
        "cite": [
            {"vol": 526, "reporter": "U.S.", "page": 489},
            {"vol": 119, "reporter": "S.Ct.", "page": 1518},
            {"vol": 143, "reporter": "L.Ed.2d", "page": 689}
        ],
        "year": 1999
    },
    {
        "style": "San Antonio Independent School District v. Rodriguez",
        "cite": [
            {"vol": 411, "reporter": "U.S.", "page": 1},
            {"vol": 93, "reporter": "S.Ct.", "page": 1278},
            {"vol": 36, "reporter": "L.Ed.2d", "page": 16}
        ],
        "year": 1973
    },
    {
        "style": "Santa Fe Independent School District v. Doe",
        "cite": [
            {"vol": 530, "reporter": "U.S.", "page": 290},
            {"vol": 120, "reporter": "S.Ct.", "page": 2266},
            {"vol": 147, "reporter": "L.Ed.2d", "page": 295}
        ],
        "year": 2000
    },
    {
        "style": "Schenck v. United States",
        "cite": [
            {"vol": 249, "reporter": "U.S.", "page": 47}
        ],
        "year": 1919
    },
    {
        "style": "Schneider v. New Jersey",
        "cite": [
            {"vol": 308, "reporter": "U.S.", "page": 147}
        ],
        "year": 1939
    },
    {
        "style": "Seminole Tribe of Florida v. Florida",
        "cite": [
            {"vol": 517, "reporter": "U.S.", "page": 44},
            {"vol": 116, "reporter": "S.Ct.", "page": 1114},
            {"vol": 134, "reporter": "L.Ed.2d", "page": 252}
        ],
        "year": 1996
    },
    {
        "style": "Shaw v. Murphy",
        "cite": [
            {"vol": 532, "reporter": "U.S.", "page": 223}
        ],
        "year": 2001
    },
    {
        "style": "Shelby County v. Holder",
        "cite": [
            {"vol": 570, "reporter": "U.S.", "page": 529},
            {"vol": 133, "reporter": "S.Ct.", "page": 2612},
            {"vol": 186, "reporter": "L.Ed.2d", "page": 651}
        ],
        "year": 2013
    },
    {
        "style": "Shelley v. Kraemer",
        "cite": [
            {"vol": 334, "reporter": "U.S.", "page": 1}
        ],
        "year": 1948
    },
    {
        "style": "Sherbert v. Verner",
        "cite": [
            {"vol": 374, "reporter": "U.S.", "page": 398}
        ],
        "year": 1963
    },
    {
        "style": "Singleton v. Wulff",
        "cite": [
            {"vol": 428, "reporter": "U.S.", "page": 106}
        ],
        "year": 1976
    },
    {
        "style": "Skinner v. Oklahoma",
        "cite": [
            {"vol": 316, "reporter": "U.S.", "page": 535}
        ],
        "year": 1942
    },
    {
        "style": "Slaughter House Cases: Butchers' Benevolent Assn. of New Orleans v. Crescent City Livestock Landing & Slaughter-house Co.",
        "cite": [
            {"vol": 83, "reporter": "U.S.", "page": 36}
        ],
        "year": 1872
    },
    {
        "style": "Snyder v. Phelps",
        "cite": [
            {"vol": 562, "reporter": "U.S.", "page": 443}
        ],
        "year": 2011
    },
    {
        "style": "South Carolina State Highway Dept. v. Barnwell Bros., Inc.",
        "cite": [
            {"vol": 303, "reporter": "U.S.", "page": 177}
        ],
        "year": 1938
    },
    {
        "style": "South-Central Timber Development, Inc. v. Wunnicke, Commissioner, Dept. of Natural Resources of Alaska",
        "cite": [
            {"vol": 467, "reporter": "U.S.", "page": 82},
            {"vol": 104, "reporter": "S.Ct.", "page": 2237}
        ],
        "year": 1984
    },
    {
        "style": "South Dakota v. Dole",
        "cite": [
            {"vol": 483, "reporter": "U.S.", "page": 203}
        ],
        "year": 1987
    },
    {
        "style": "Southern Pacific Co. v. Arizona Ex Rel. Sullivan, Attorney General",
        "cite": [
            {"vol": 325, "reporter": "U.S.", "page": 761}
        ],
        "year": 1945
    },
    {
        "style": "Stanley v. Georgia",
        "cite": [
            {"vol": 394, "reporter": "U.S.", "page": 557}
        ],
        "year": 1969
    },
    {
        "style": "State Farm Mutual Automobile Insurance Co. v. Campbell",
        "cite": [
            {"vol": 538, "reporter": "U.S.", "page": 408}
        ],
        "year": 2003
    },
    {
        "style": "State of Minnesota v. Clover Leaf Creamery Co.",
        "cite": [
            {"vol": 449, "reporter": "U.S.", "page": 456},
            {"vol": 101, "reporter": "S.Ct.", "page": 715}
        ],
        "year": 1981
    },
    {
        "style": "Supreme Court of New Hampshire v. Piper",
        "cite": [
            {"vol": 470, "reporter": "U.S.", "page": 274},
            {"vol": 105, "reporter": "S.Ct.", "page": 1272}
        ],
        "year": 1985
    },
    {
        "style": "Swann v. Charlotte-Mecklenburg Board of Education",
        "cite": [
            {"vol": 402, "reporter": "U.S.", "page": 1}
        ],
        "year": 1971
    },
    {
        "style": "Tahoe-Sierra Preservation Council, Inc. v. Tahoe Regional Planning Agency",
        "cite": [
            {"vol": 535, "reporter": "U.S.", "page": 302}
        ],
        "year": 2002
    },
    {
        "style": "Tennessee Wine and Spirits Retailers Association v. Thomas",
        "cite": [
            {"vol": 139, "reporter": "S.Ct.", "page": 2449}
        ],
        "year": 2019
    },
    {
        "style": "Terry v. Adams",
        "cite": [
            {"vol": 345, "reporter": "U.S.", "page": 461}
        ],
        "year": 1953
    },
    {
        "style": "Texas v. Johnson",
        "cite": [
            {"vol": 491, "reporter": "U.S.", "page": 397}
        ],
        "year": 1989
    },
    {
        "style": "United States v. Stanley",
        "cite": [
            {"vol": 109, "reporter": "U.S.", "page": 3}
        ],
        "year": 1883
    },
    {
        "style": "Thomas & Windy City Hemp Development Board v. Chicago Park District",
        "cite": [
            {"vol": 534, "reporter": "U.S.", "page": 316}
        ],
        "year": 2002
    },
    {
        "style": "Thornburgh v. Abbott",
        "cite": [
            {"vol": 490, "reporter": "U.S.", "page": 401}
        ],
        "year": 1989
    },
    {
        "style": "Timbs v. Indiana",
        "cite": [
            {"vol": 139, "reporter": "S.Ct.", "page": 682}
        ],
        "year": 2019
    },
    {
        "style": "Tinker v. Des Moines Independent Community School District",
        "cite": [
            {"vol": 393, "reporter": "U.S.", "page": 503},
            {"vol": 89, "reporter": "S.Ct.", "page": 733}
        ],
        "year": 1969
    },
    {
        "style": "Toomer v. Witsell",
        "cite": [
            {"vol": 334, "reporter": "U.S.", "page": 385}
        ],
        "year": 1948
    },
    {
        "style": "Town of Greece v. Galloway",
        "cite": [
            {"vol": 572, "reporter": "U.S.", "page": 565}
        ],
        "year": 2014
    },
    {
        "style": "Troxel v. Granville",
        "cite": [
            {"vol": 530, "reporter": "U.S.", "page": 57}
        ],
        "year": 2000
    },
    {
        "style": "Trump v. Hawaii",
        "cite": [
            {"vol": 138, "reporter": "S.Ct.", "page": 2392},
            {"vol": 201, "reporter": "L.Ed.2d", "page": 403}
        ],
        "year": 2018
    },
    {
        "style": "Turner Broadcasting System, Inc. v. Federal Communications Commn.",
        "cite": [
            {"vol": 512, "reporter": "U.S.", "page": 622}
        ],
        "year": 1994
    },
    {
        "style": "Twining v. New Jersey",
        "cite": [
            {"vol": 211, "reporter": "U.S.", "page": 78}
        ],
        "year": 1908
    },
    {
        "style": "United Building & Construction Trades Council of Camden County v. Mayor & Council of the City of Camden",
        "cite": [
            {"vol": 465, "reporter": "U.S.", "page": 208}
        ],
        "year": 1984
    },
    {
        "style": "United Haulers Assn., Inc. v. Oneida-Herkimer Solid Waste Management Authority",
        "cite": [
            {"vol": 550, "reporter": "U.S.", "page": 330},
            {"vol": 127, "reporter": "S.Ct.", "page": 1786}
        ],
        "year": 2007
    },
    {
        "style": "United States Parole Commission v. Geraghty",
        "cite": [
            {"vol": 445, "reporter": "U.S.", "page": 388}
        ],
        "year": 1980
    },
    {
        "style": "United States Railroad Retirement Board v. Fritz",
        "cite": [
            {"vol": 449, "reporter": "U.S.", "page": 166}
        ],
        "year": 1980
    },
    {
        "style": "United States Trust Co. v. New Jersey",
        "cite": [
            {"vol": 431, "reporter": "U.S.", "page": 1},
            {"vol": 97, "reporter": "S.Ct.", "page": 1505},
            {"vol": 52, "reporter": "L.Ed.2d", "page": 92}
        ],
        "year": 1977
    },
    {
        "style": "United States v. American Library Assn., Inc.",
        "cite": [
            {"vol": 539, "reporter": "U.S.", "page": 194},
            {"vol": 123, "reporter": "S.Ct.", "page": 2297},
            {"vol": 156, "reporter": "L.Ed.2d", "page": 221}
        ],
        "year": 2003
    },
    {
        "style": "United States v. Ballard",
        "cite": [
            {"vol": 322, "reporter": "U.S.", "page": 78}
        ],
        "year": 1944
    },
    {
        "style": "United States v. Butler",
        "cite": [
            {"vol": 297, "reporter": "U.S.", "page": 1}
        ],
        "year": 1936
    },
    {
        "style": "United States v. Carolene Products Co.",
        "cite": [
            {"vol": 304, "reporter": "U.S.", "page": 144}
        ],
        "year": 1938
    },
    {
        "style": "United States v. Comstock",
        "cite": [
            {"vol": 560, "reporter": "U.S.", "page": 126}
        ],
        "year": 2010
    },
    {
        "style": "United States v. Curtiss-Wright Export Corp.",
        "cite": [
            {"vol": 299, "reporter": "U.S.", "page": 304},
            {"vol": 57, "reporter": "S.Ct.", "page": 216}
        ],
        "year": 1936
    },
    {
        "style": "United States v. Darby",
        "cite": [
            {"vol": 312, "reporter": "U.S.", "page": 100},
            {"vol": 61, "reporter": "S.Ct.", "page": 451}
        ],
        "year": 1941
    },
    {
        "style": "United States v. E.C. Knight Co.",
        "cite": [
            {"vol": 156, "reporter": "U.S.", "page": 1},
            {"vol": 15, "reporter": "S.Ct.", "page": 249}
        ],
        "year": 1895
    },
    {
        "style": "United States v. Georgia",
        "cite": [
            {"vol": 546, "reporter": "U.S.", "page": 151}
        ],
        "year": 2006
    },
    {
        "style": "United States v. Klein",
        "cite": [
            {"vol": 80, "reporter": "U.S.", "page": 128}
        ],
        "year": 1872
    },
    {
        "style": "United States v. Kokinda",
        "cite": [
            {"vol": 497, "reporter": "U.S.", "page": 720}
        ],
        "year": 1990
    },
    {
        "style": "United States v. Kras",
        "cite": [
            {"vol": 409, "reporter": "U.S.", "page": 434}
        ],
        "year": 1973
    },
    {
        "style": "United States v. Lopez",
        "cite": [
            {"vol": 514, "reporter": "U.S.", "page": 549}
        ],
        "year": 1995
    },
    {
        "style": "United States v. Morrison",
        "cite": [
            {"vol": 529, "reporter": "U.S.", "page": 598}
        ],
        "year": 2000
    },
    {
        "style": "United States v. National Treasury Employees Union",
        "cite": [
            {"vol": 513, "reporter": "U.S.", "page": 454}
        ],
        "year": 1995
    },
    {
        "style": "United States v. Nixon",
        "cite": [
            {"vol": 418, "reporter": "U.S.", "page": 683},
            {"vol": 94, "reporter": "S.Ct.", "page": 3090}
        ],
        "year": 1974
    },
    {
        "style": "United States v. O'Brien",
        "cite": [
            {"vol": 391, "reporter": "U.S.", "page": 367}
        ],
        "year": 1968
    },
    {
        "style": "United States v. Richardson",
        "cite": [
            {"vol": 418, "reporter": "U.S.", "page": 166}
        ],
        "year": 1974
    },
    {
        "style": "United States v. Seeger",
        "cite": [
            {"vol": 380, "reporter": "U.S.", "page": 163}
        ],
        "year": 1965
    },
    {
        "style": "United States v. Stevens",
        "cite": [
            {"vol": 559, "reporter": "U.S.", "page": 460},
            {"vol": 130, "reporter": "S.Ct.", "page": 1577}
        ],
        "year": 2010
    },
    {
        "style": "United States v. Virginia",
        "cite": [
            {"vol": 518, "reporter": "U.S.", "page": 515},
            {"vol": 116, "reporter": "S.Ct.", "page": 2264},
            {"vol": 135, "reporter": "L.Ed.2d", "page": 735}
        ],
        "year": 1996
    },
    {
        "style": "United States v. Windsor",
        "cite": [
            {"vol": 570, "reporter": "U.S.", "page": 744},
            {"vol": 133, "reporter": "S.Ct.", "page": 2675},
            {"vol": 186, "reporter": "L.Ed.2d", "page": 808}
        ],
        "year": 2013
    },
    {
        "style": "U.S. Dept. of Agriculture v. Moreno",
        "cite": [
            {"vol": 413, "reporter": "U.S.", "page": 528},
            {"vol": 93, "reporter": "S.Ct.", "page": 2821}
        ],
        "year": 1973
    },
    {
        "style": "Van Orden v. Perry",
        "cite": [
            {"vol": 545, "reporter": "U.S.", "page": 677}
        ],
        "year": 2005
    },
    {
        "style": "Vieth v. Jubelirer",
        "cite": [
            {"vol": 541, "reporter": "U.S.", "page": 267}
        ],
        "year": 2004
    },
    {
        "style": "Village of Arlington Heights v. Metropolitan Housing Development Corp.",
        "cite": [
            {"vol": 429, "reporter": "U.S.", "page": 252}
        ],
        "year": 1977
    },
    {
        "style": "Virginia State Board of Pharmacy v. Virginia Citizens Consumer Council, Inc.",
        "cite": [
            {"vol": 425, "reporter": "U.S.", "page": 748}
        ],
        "year": 1976
    },
    {
        "style": "Virginia v. Black",
        "cite": [
            {"vol": 538, "reporter": "U.S.", "page": 343},
            {"vol": 123, "reporter": "S.Ct.", "page": 1536},
            {"vol": 155, "reporter": "L.Ed.2d", "page": 535}
        ],
        "year": 2003
    },
    {
        "style": "Walker v. Texas Division, Sons of Confederate Veterans",
        "cite": [
            {"vol": 576, "reporter": "U.S.", "page": 200},
            {"vol": 135, "reporter": "S.Ct.", "page": 2239},
            {"vol": 192, "reporter": "L.Ed.2d", "page": 274}
        ],
        "year": 2015
    },
    {
        "style": "Ward v. Rock Against Racism",
        "cite": [
            {"vol": 491, "reporter": "U.S.", "page": 781}
        ],
        "year": 1989
    },
    {
        "style": "Washington v. Davis",
        "cite": [
            {"vol": 426, "reporter": "U.S.", "page": 229}
        ],
        "year": 1976
    },
    {
        "style": "Washington v. Glucksberg",
        "cite": [
            {"vol": 521, "reporter": "U.S.", "page": 702},
            {"vol": 117, "reporter": "S.Ct.", "page": 2258},
            {"vol": 138, "reporter": "L.Ed.2d", "page": 772}
        ],
        "year": 1997
    },
    {
        "style": "Watchtower Bible & Tract Society of New York, Inc. v. Village of Stratton",
        "cite": [
            {"vol": 536, "reporter": "U.S.", "page": 150}
        ],
        "year": 2002
    },
    {
        "style": "Weaver v. Palmer Bros. Co.",
        "cite": [
            {"vol": 270, "reporter": "U.S.", "page": 402}
        ],
        "year": 1926
    },
    {
        "style": "West Coast Hotel Co. v. Parrish",
        "cite": [
            {"vol": 300, "reporter": "U.S.", "page": 379}
        ],
        "year": 1937
    },
    {
        "style": "Western & Southern Life Insurance Co. v. State Board of Equalization of California",
        "cite": [
            {"vol": 451, "reporter": "U.S.", "page": 648}
        ],
        "year": 1981
    },
    {
        "style": "West Lynn Creamery, Inc. v. Healy",
        "cite": [
            {"vol": 512, "reporter": "U.S.", "page": 186},
            {"vol": 114, "reporter": "S.Ct.", "page": 2205},
            {"vol": 129, "reporter": "L.Ed.2d", "page": 157}
        ],
        "year": 1994
    },
    {
        "style": "West Virginia State Board of Education v. Barnette",
        "cite": [
            {"vol": 319, "reporter": "U.S.", "page": 624},
            {"vol": 63, "reporter": "S.Ct.", "page": 1178}
        ],
        "year": 1943
    },
    {
        "style": "Whalen v. Roe",
        "cite": [
            {"vol": 429, "reporter": "U.S.", "page": 589}
        ],
        "year": 1977
    },
    {
        "style": "Whitman v. American Trucking Associations, Inc.",
        "cite": [
            {"vol": 531, "reporter": "U.S.", "page": 457}
        ],
        "year": 2001
    },
    {
        "style": "Whitney v. California",
        "cite": [
            {"vol": 274, "reporter": "U.S.", "page": 357}
        ],
        "year": 1927
    },
    {
        "style": "Whole Woman's Health v. Hellerstedt",
        "cite": [
            {"vol": 136, "reporter": "S.Ct.", "page": 2292}
        ],
        "year": 2016
    },
    {
        "style": "Wickard v. Filburn",
        "cite": [
            {"vol": 317, "reporter": "U.S.", "page": 111},
            {"vol": 63, "reporter": "S.Ct.", "page": 82}
        ],
        "year": 1942
    },
    {
        "style": "Williamson v. Lee Optical of Oklahoma, Inc.",
        "cite": [
            {"vol": 348, "reporter": "U.S.", "page": 483}
        ],
        "year": 1955
    },
    {
        "style": "Williams-Yulee v. Florida Bar",
        "cite": [
            {"vol": 575, "reporter": "U.S.", "page": 433}
        ],
        "year": 2015
    },
    {
        "style": "Youngstown Sheet & Tube Co. v. Sawyer",
        "cite": [
            {"vol": 343, "reporter": "U.S.", "page": 579},
            {"vol": 72, "reporter": "S.Ct.", "page": 863}
        ],
        "year": 1952
    },
    {
        "style": "Young v. American Mini Theatres, Inc.",
        "cite": [
            {"vol": 427, "reporter": "U.S.", "page": 50},
            {"vol": 96, "reporter": "S.Ct.", "page": 2440}
        ],
        "year": 1976
    },
    {
        "style": "Zablocki v. Redhail",
        "cite": [
            {"vol": 434, "reporter": "U.S.", "page": 374}
        ],
        "year": 1978
    },
    {
        "style": "Zelman v. Simmons-Harris",
        "cite": [
            {"vol": 536, "reporter": "U.S.", "page": 639},
            {"vol": 122, "reporter": "S.Ct.", "page": 2460}
        ],
        "year": 2002
    },
    {
        "style": "Zivotofsky ex rel. Zivotofsky v. Kerry (Zivotofsky II)",
        "cite": [
            {"vol": 576, "reporter": "U.S.", "page": 1}
        ],
        "year": 2015
    }
]
}
@endjson
```