#%%
import os
import requests
import datetime

#%%
class Cap(object):
    """
    Adapted from CAP, this class is used for accessing the API from the Harvard Law Caselaw Access Project to pull JSON data by case.
     
    """

    def __init__(self):
        """
        Used for authentication.
        """
        self.API_KEY = os.getenv('API_KEY')
        self.API_URL = os.getenv('API_URL')
        self.API_VERSION = os.getenv('API_VERSION')
        self.header = {'AUTHORIZATION': f'Token {self.API_KEY}'}

    def _get_api_url(self):
        """
        Internal method for retrieving base API URL from settings.
        """
        return f"{self.API_URL}/{self.API_VERSION}/"

    def _request(self, url):
        """
        Internal method for making API requests.
        """
        response = requests.get(url, headers=self.header)
        statCode = str(response.status_code)

        if statCode.startswith('2'):
            return response
        else:
            raise Exception(f"URI request returned an error. Error Code {statCode}")

    def _build_uri(self, uri_base, params):
        """
        Internal method for constructing search query URIs with multiple parameters.
        """
        if not params:
            return uri_base
        else:
            uri_extension = "?"
            for param in params:
                uri_extension = uri_extension + param + "&"
            uri_extension = uri_extension[:-1]  # clip off the final & 
            uri = uri_base + uri_extension
            return uri

    def _extract_from_paginated(self, first_page, attribute_name):
        """
        Internal method for retrieving a list of each specified attribute from a given paginated JSON.
        e.g.: _extract_from_paginated(some_paginated_list, "name") would return an array with the list of 
        all the court names from the given paginated list.
        """
        names = []
        current_page = first_page

        while True:
            names = names + [court[attribute_name] for court in current_page["results"]]
            try:
                next_result = self._request(current_page["next"])
                current_page = next_result.json()
            except:
                break

        return names

    def get_case(self, case_id, full_case=False):
        """
        Single case endpoint; retrieve a case by its numeric ID.
        
        :param case_id: numeric ID used to identify case 
        :type case_id: str|int
        :param full_case: when set to true, this parameter loads the full text. default False.
                          keep in mind this counts toward daily limit for non-research accounts.
        :type full_case: boolean
        
        :return: Case information in JSON
        """
        url = self._get_api_url() + "cases/" + str(case_id)

        if (full_case):
            url = url + "/?full_case=true"

        case = self._request(url)
        return case.json()

    def search_cases(self, search_term="", jurisdiction="", court="", author="", name_abbreviation="", citation="", decision_date_min="", decision_date_max="", full_case=False, uri_only=False):
        """
        Full case search endpoint; retrieve list of cases matching specified parameters.
        All parameters optional (and defined as empty by default). 
        
        :param search_term: search by given word; full text search query.
                            multiple search terms can be used by adding a space (ie, "Florida bankruptcy"
                            will only return cases that contain both Florida AND bankruptcy)
        :type case_id: str
        :param jurisdiction: search by jurisdiction; takes a jurisdiction slug
        :type jurisdiction: str
        :param court: Search by court; takes a court slug. Can only specify one slug.
                      See multi_search_cases to specifiy multiple court slugs.
        :type court: str
        :param author: search by author; use opinion author's last name.
        :type author: str
        :param name_abbreviation: search by case style
        :type name_abbreviation: str
        :param citation: search by case citation
        :type citation: str
        :param decision_date_min: search by earliest date; YYYY-MM-DD format
        :type decision_date_min: string
        :param decision_date_max: search by maximum date; YYYY-MM-DD format
        :type decision_date_max: string
        :param full_case: when set to true, full text and body will be loaded for all cases.
                          default 'false'. keep in mind this counts toward daily limit for non-research 
                          accounts.
        :type full_case: boolean
        :param uris_only: When set to True, returns only the URI, not the results of the URI request.
        :type uris_only: boolean
        
        :return: Paginated and ordered JSON list with case info JSON for each case
        """
        url_base = self._get_api_url() + "cases/"
        url_queries = []

        if search_term:
            url_queries.append("search=%s&full_case=true" % search_term)

        if jurisdiction:
            jurisdiction = jurisdiction.lower()
            valid_jurisdictions = [elem['slug'] for elem in self.get_jurisdictions()["results"]]
            if jurisdiction not in valid_jurisdictions:
                raise Exception("Jurisdiction not recognized. Check spelling?")
            url_queries.append("jurisdiction=%s" % jurisdiction)

        if court:
            court = court.lower()
            url_queries.append("court=%s" % court)
        
        if author:
            url_queries.append(f'author={author}')
        
        if  name_abbreviation:
            url_queries.append(f'name_abbreviation="{name_abbreviation}"')
        
        if citation:
            url_queries.append(f'cite={citation}')
            
        if decision_date_min:
            try:
                datetime.datetime.strptime(decision_date_min, "%Y-%m-%d")
                url_queries.append("decision_date_min=%s" % decision_date_min)
            except:
                raise Exception("Invalid decision_date_min. Make sure date is formatted YYYY-MM-DD.")

        if decision_date_max:
            try:
                datetime.datetime.strptime(decision_date_max, "%Y-%m-%d")
                url_queries.append("decision_date_max=%s" % decision_date_max)
            except:
                raise Exception("Invalid decision_date_max. Make sure date is formatted YYYY-MM-DD.")

        if full_case:
            url_queries.append("full_case=true")

        uri = self._build_uri(url_base, url_queries)

        if uri_only:
            return uri

        search_results = self._request(uri)
        return search_results.json()


# %%
