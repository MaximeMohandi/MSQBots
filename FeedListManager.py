import json

listFeed = 'FluxFileMSQbitsReporter.json'

#get the feed source
def GetTheList(cat='all'):
    with open(listFeed) as json_file:
        if(cat.upper() == 'ALL'):
            return json.load(json_file)
        else:
            return [i for i in json.load(json_file) if i['categorie'] == cat.upper()]
 
#add a link in the json file
def AddFeedInList(id,nom,site,lien,categorie):
    data =GetTheList()
    data.append({
            'id':id,
            'nom':nom,
            'site':site,
            'lien':lien,
            'categorie':categorie
        })
    
    with open(listFeed,'w') as outfile:
        json.dump(data,outfile)

#delete one elt from the list
def DelFeedInList(id):
    data =GetTheList()
    data.pop(id)
    
    with open(listFeed,'w') as outfile:
        json.dump(data,outfile)