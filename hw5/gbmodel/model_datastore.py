# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .Model import Model
from datetime import datetime
from google.cloud import datastore

def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        [ name, streetAddress, city, state, zipCode, hours, phone, rating, review, drink]
        where all are python strings
    """
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [entity['name'],entity['streetAddress'],entity['city'],entity['state'],entity['zipCode'],entity['hours'],entity['phone'],entity['rating'],entity['review'],entity['drink'],entity['analysis']]

class model(Model):
    def __init__(self):
        self.client = datastore.Client('cs430-lily-tran')

    def select(self):
        query = self.client.query(kind = 'bubbletea')
        entities = list(map(from_datastore,query.fetch()))
        return entities

    def insert(self,name,streetAddress,city,state,zipCode,hours,phone,rating,review,drink,analysis):
        key = self.client.key('bubbletea')
        rev = datastore.Entity(key)
        rev.update( {
            'name' : name,
            'streetAddress' : streetAddress,
            'city' : city,
            'state' : state,
            'zipCode' : zipCode,
            'hours' : hours,
            'phone' : phone,
            'rating' : rating,
            'review' : review,
            'drink' : drink,
            'analysis' : analysis
            })
        self.client.put(rev)
        return True
