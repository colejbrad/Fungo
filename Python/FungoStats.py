# Create basic stats
import pandas as pd
from FungoSplits import FungoSplits as fs
from FungoImport import FungoImport as fi


class FungoStats:

    hitTypes = {'hits': ['single', 'double', 'triple', 'hr'],
                'reachSafe': ['roe', 'fc', 'kpb'],
                'sacs': ['sb', 'sh', 'sf'],
                'nonHits': ['walk', 'hbp'],
                'outs': ['fo3', 'fo4', 'fo5', 'fo6', 'fo7', 'fo8', 'fo9',
                         'go1', 'go2', 'go3', 'go4', 'go5', 'go6',
                         'lo1', 'lo3', 'lo4', 'lo5', 'lo6', 'lo7', 'lo8', 'lo9',
                         'po1', 'po2', 'po3', 'po4', 'po5', 'po6',
                         'gidp', 'k', 'kk']}

    def average(playerData):
        global hitTypes
        hits = 0
        atBats = 0
        for index, row in playerData.iterrows():
            if row['hitType'] == '':
                continue

            if row['hitType'] in hitTypes['hits']:
                hits += 1
                atBats += 1
            elif row['hitType'] in hitTypes['outs'] or hitTypes['reachSafe']:
                atBats += 1

        return hits / atBats

    def whiffRate(playerData):
        swings = 0
        misses = 0
        for index, row in playerData.iterrows():
            if row['miss'] == 1:
                swings += 1
                misses += 1
            elif row['swing'] == 1:
                swings += 1

        return misses / swings

    def onBase(playerData):
        global hitTypes
        onBase = 0
        plateAppearance = len(playerData)
        for index, row in playerData.iterrows():
            if row['hitType'] in hitTypes['hits'] or hitTypes['reachSafe']:
                onBase += 1
            elif row['result'] in hitTypes['nonhits']:
                onBase += 1

        return onBase / plateAppearance

    def slugging(playerData):
        global hitTypes
        hits = 0
        atBats = 0
        for index, row in playerData.iterrows():
            if row['hitType'] == '' or row['hitType'] in hitTypes['sacs']:
                continue

            match row['hitType']:
                case 'single':
                    hits += 1
                    atBats += 1
                case 'double':
                    hits += 2
                    atBats += 1
                case 'triple':
                    hits += 3
                    atBats += 1
                case 'hr':
                    hits += 4
                    atBats += 1
                case _:
                    atBats += 1

        return hits / atBats


hitterNew = fi.importHitter('Output_CSV\\SnelsonResults.csv')
SnelsonAVG = FungoStats.average(hitterNew)
SnelsonWhiff = FungoStats.whiffRate(hitterNew)
SnelsonOBP = FungoStats.onBase(hitterNew)
