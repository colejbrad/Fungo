# Create basic stats


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

    def average(self, playerData):
        '''
        Calculate a hitter's batting average

        Parameters
        ----------
        playerData : DataFrame
            DataFrame of a hitter's plate appearances

        Returns
        -------
        float
            The hitter's batting average

        '''
        hits = 0
        atBats = 0
        for index, row in playerData.iterrows():
            if row['hitType'] == '':
                continue

            if row['hitType'] in self.hitTypes['hits']:
                hits += 1
                atBats += 1
            elif row['hitType'] in self.hitTypes['outs'] or self.hitTypes['reachSafe']:
                atBats += 1

        if atBats == 0:
            return 0
        return hits / atBats

    def whiffRate(self, playerData):
        '''
        Calculate a hitter's swing and miss rate

        Parameters
        ----------
        playerData : DataFrame
            DataFrame of a hitter's plate appearances

        Returns
        -------
        float
            The batter's swing and miss rate

        '''
        swings = 0
        misses = 0
        for index, row in playerData.iterrows():
            if row['swing'] == 1:
                swings += 1
                if row['miss'] == 1:
                    misses += 1

        return misses / swings

    def onBase(self, playerData):
        '''
        Calculate a hitter's on base percentage

        Parameters
        ----------
        playerData : DataFrame
            DataFrame of a hitter's plate appearances

        Returns
        -------
        float
            The hitter's on base percentage

        '''
        onBase = 0
        plateAppearance = len(playerData)
        for index, row in playerData.iterrows():
            if (row['hitType'] in self.hitTypes['hits'] or row['hitType'] in self.hitTypes['reachSafe'] or row['resultType'] in self.hitTypes['nonHits']):
                onBase += 1

        return onBase / plateAppearance

    def slugging(self, playerData):
        '''
        Calculate a hitter's slugging percentage

        Parameters
        ----------
        playerData : DataFrame
            DataFrame of a hitter's plate appearances

        Returns
        -------
        float
            The hitter's slugging percentage

        '''
        hits = 0
        atBats = 0
        for index, row in playerData.iterrows():
            if row['hitType'] == '' or row['hitType'] in self.hitTypes['sacs']:
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

    def iso(self, playerData):
        '''
        Calculate a hitter's isolated power (percentage of XBH)

        Parameters
        ----------
        playerData : DataFrame
            DataFrame of a hitter's plate appearances

        Returns
        -------
        float
            A player's isolated power

        '''
        return self.slugging(playerData) - self.average(playerData)

    def walkPct(self, playerData):
        '''
        Calculates the percentage of a hitter's plate appearances that result in
        a walk

        Parameters
        ----------
        playerData : DataFrame
            DataFrame of a hitter's plate appearances

        Returns
        -------
        Float
            The hitter's walk rate

        '''
        walkCount = 0
        for index, row in playerData.iterrows():
            if row['resultType'] == 'walk':
                walkCount += 1

        return walkCount / len(playerData)

    def strikeoutPct(self, playerData):
        '''
        Calculates the percentage of a hitter's plate appearances that result in
        a strikeout

        Parameters
        ----------
        playerData : DataFrame
            DataFrame of a hitter's plate appearances

        Returns
        -------
        Float
            The hitter's strikeout rate

        '''
        kCount = 0
        for index, row in playerData.iterrows():
            if row['hitType'] in ['k', 'kk']:
                kCount += 1

        return kCount / len(playerData)

    def fieldRatios(self, playerData):
        '''
        Calculates the percentage a player's batted balls go to each field

        Parameters
        ----------
        playerData : DataFrame
            DataFrame of a hitter's plate appearances

        Returns
        -------
        Tuple
            A tuple containing the percentage of hits to each field in the order
                (left, center, right)

        '''
        left = 0
        center = 0
        right = 0
        bip = 0

        for index, row in playerData.iterrows():
            if row['result'] == 'bip':
                bip += 1

            if row['resultLocation'] in [1, 6, 7]:
                right += 1
            elif row['resultLocation'] in [2, 5]:
                center += 1
            elif row['resultLocation'] in [3, 4, 8]:
                left += 1

        return (left / bip, center / bip, right / bip)

    def hitTypeRatios(self, playerData):
        '''
        Calculate the percentage of a player's balls in play that are of varying
        types (grounders, liners, fly balls)

        Parameters
        ----------
        playerData : DataFrame
            DataFrame of a hitter's plate appearances

        Returns
        -------
        Tuple
            A tuple containing the percentage of balls that are of each types in
            the order: (grounder, liner, fly)

        '''
        grounder = 0
        liner = 0
        fly = 0
        bip = 0

        for index, row in playerData.iterrows():
            if row['result'] == 'bip':
                bip += 1

            if row['hitType'][0:2] == 'sb' or row['resultType'] == 'popup':
                continue

            match row['resultType']:
                case 'grounder':
                    grounder += 1
                case 'liner':
                    liner += 1
                case 'fly':
                    fly += 1
                case _:
                    continue

        return (grounder / bip, liner / bip, fly / bip)

    def chaseRate(self, playerData):
        '''
        Calculates the percent of swing and misses a player has out of all
        swings on balls out of the zone

        Parameters
        ----------
        playerData : DataFrame
            DataFrame of a hitter's plate appearances

        Returns
        -------
        Float
            A player's chase rate

        '''
        ooz = 0
        chase = 0

        for index, row in playerData.iterrows():
            if row['pitchLocation'] > 9:
                ooz += 1
                if row['swing'] == 1:
                    chase += 1

        return chase / ooz
