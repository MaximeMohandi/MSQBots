from datetime import datetime, timedelta
import FeedListManager as fm
import logging
import feedparser


#displau all the info
async def DisplayAll(ctx,arg=4):
    try:
        for i in fm.GetTheList():
            
            await ctx.send(
                """_ _{0}**📰  {1}   📰** - <{2}>\n***🔖 {3}***""".format('\n',i['nom'],i['site'],i['categorie']))

            NewsFeed = feedparser.parse(i['lien'])
            count = int(arg)
            for j in NewsFeed.entries:
                if(j.published_parsed.tm_mday > datetime.now().day -2):
                    count -= 1
                    if count != 0:
                        await ctx.send("""**{0}**\n<{1}>\n*{2}*""".format(j.title,j.link,j.published))
                    
    except Exception as ex:
        await ctx.send(ex)
        await ctx.message.add_reaction('❌')

#display specific cat
async def DisplaySpecial(ctx, *args):
    try:

        data=args[0]

        nom=data[0]
        nbArticle=int(data[1])
        
        for i in fm.GetTheList():
            if i['nom'].upper() == nom.upper():
                await ctx.send(
                """_ _{0}**📰  {1}   📰** - <{2}>\n***🔖 {3}***""".format('\n',i['nom'],i['site'],i['categorie']))

                NewsFeed = feedparser.parse(i['lien'])
                for j in NewsFeed.entries:
                    nbArticle -= 1
                    await ctx.send("""**{0}**\n<{1}>\n*{2}*\n""".format(j.title,j.link,j.published))
                    if nbArticle == 0 :
                        break
    except Exception as ex:
        print(ex)
        await ctx.message.add_reaction('❌')
    
    

#Add a feed in the Json and print a reaction for resl=ult
async def AddFeed(ctx, *arg):
    try:
        data = arg[0]
        fm.AddFeedInList(
            id=fm.GetTheList()[-1]['id']+1,
            nom=data[0],
            site=data[1],
            lien=data[2],
            categorie=data[3]
        )
        await ctx.message.add_reaction('✅')
    except Exception as ex:
        print(ex)
        await ctx.message.add_reaction('❌')

#display available category
async def DisplayFeedCategory(ctx,arg):
    try:
        cat =[]
        message =''
        for elt in fm.GetTheList(arg):
            if elt['categorie'] not in cat:
                cat.append(elt['categorie'])

        for x in cat:
            message+='__**{0}**__\n'.format(str(x))
            for i in fm.GetTheList(x):
                message+='{0} - {1} : <{2}>\n'.format(i['id'],i['nom'],i['site'])
        await ctx.send(message)
    except Exception as ex:
        print(ex)
        await ctx.message.add_reaction('❌')


#delete a feed from the json list
async def DeleteFeed(ctx,arg):
    try:
        fm.DelFeedInList(int(arg)-1)
        await ctx.message.add_reaction('✅')
    except Exception as ex:
        print(ex)
        await ctx.message.add_reaction('❌')