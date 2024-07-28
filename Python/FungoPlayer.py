# Create a dictionary containing information about a player for use in output PDFs
import os
from FungoImport import FungoImport as fi
from FungoSplits import FungoSplits as fs
from FungoStats import FungoStats as fStat


class FungoPlayer:
    def createPlayer(playerName: str) -> dict:
        """
        Creates a dictionary containing a player's name and many of their stats such as
        average, on base percentage, slugging, etc.

        Parameters
        ----------
        playerName : str
            The last name of a player, title case

        Returns
        -------
        dict
            Dictionary of a player's name and stats

        """
        try:
            # Create DataFrames
            player = FungoPlayer.getDataFrames(playerName)

            # Dictionary storing information about a player
            playerDict = {}

            # Set the player's name
            playerDict["Name"] = playerName

            # Set values for various statistics for the player
            # Tuples are set up as (Total, vs Right, vs Left)
            playerDict["avg"] = FungoPlayer.getAverages(playerName)
            playerDict["obp"] = FungoPlayer.getOBP(playerName)
            playerDict["slg"] = FungoPlayer.getSLG(playerName)
            playerDict["iso"] = FungoPlayer.getISO(playerName)
            playerDict["walkPct"] = FungoPlayer.getWalkPct(playerName)
            playerDict["kPct"] = FungoPlayer.getKPct(playerName)

            # Only have values for Total since they use full DataFrame
            playerDict["whiffPct"] = fStat.whiffRate(player[0])
            playerDict["ChasePct"] = fStat.chaseRate(player[0])

            # This tuple is set up as (Left, Center, Right)
            playerDict["FieldPcts"] = fStat.fieldRatios(player[1])

            # This tuple is set up as (Grounder, Liner, Fly ball)
            playerDict["HitTypes"] = fStat.hitTypeRatios(player[1])

            return playerDict
        except ValueError:
            print("Input must be of type: str")

    def getDataFrames(playerName: str) -> tuple:
        """
        Creates Pandas DataFrames for a specified player

        Parameters
        ----------
        playerName : str
            The last name of a player, title case

        Returns
        -------
        tuple
            A tuple with the following elements: a DataFrame containing information for
            every pitch the player saw, a DataFrame of the result of each of a player's
            plate appearances, and a tuple containing 2 DataFrames: plate appearances vs
            lefty pitchers and plate appearances vs righty pitchers

        """
        try:
            # Change path to correct location on user's disk
            os.chdir("C:\\Users\\1030c\\Desktop\\Fungo\\Fungo\\")

            # Create DataFrames containing info on specified player
            playerDF = fi.importHitter(f"Output_CSV\\{playerName}.csv")
            playerResultsDF = fi.importHitter(f"Output_CSV\\{playerName}Results.csv")
            handSplitsDF = fs.getSplitHitterPAs(playerResultsDF)

            return (playerDF, playerResultsDF, handSplitsDF)
        except ValueError:
            print("Input must be of type: str")

    def getAverages(playerName: str) -> tuple:
        """
        Getter method for a player's batting average

        Parameters
        ----------
        playerName : str
            The last name of a player, title case

        Returns
        -------
        tuple
            A tuple containing a player's overall batting average, as well as batting
            average against LHP and RHP

        """
        player = FungoPlayer.getDataFrames(playerName)

        return (
            fStat.average(player[1]),
            fStat.average(player[2][0]),
            fStat.average(player[2][1]),
        )

    def getOBP(playerName: str) -> tuple:
        """
        Getter method for a player's on base percentage

        Parameters
        ----------
        playerName : str
            The last name of a player, title case

        Returns
        -------
        tuple
            A tuple containing a player's overall on base percentage, as well as on base
            percentage against LHP and RHP

        """
        player = FungoPlayer.getDataFrames(playerName)

        return (
            fStat.onBase(player[1]),
            fStat.onBase(player[2][0]),
            fStat.onBase(player[2][1]),
        )

    def getSLG(playerName: str) -> tuple:
        """
        Getter method for a player's slugging percentage

        Parameters
        ----------
        playerName : str
            The last name of a player, title case

        Returns
        -------
        tuple
            A tuple containing a player's overall slugging percentage, as well as slugging
            percentage against LHP and RHP

        """
        player = FungoPlayer.getDataFrames(playerName)

        return (
            fStat.slugging(player[1]),
            fStat.slugging(player[2][0]),
            fStat.slugging(player[2][1]),
        )

    def getISO(playerName: str) -> tuple:
        """
        Getter method for a player's isolated power

        Parameters
        ----------
        playerName : str
            The last name of a player, title case

        Returns
        -------
        tuple
            A tuple containing a player's overall isolated power, as well as isolated
            power against LHP and RHP

        """
        player = FungoPlayer.getDataFrames(playerName)

        return (fStat.iso(player[1]), fStat.iso(player[2][0]), fStat.iso(player[2][1]))

    def getWalkPct(playerName: str) -> tuple:
        """
        Getter method for a player's walk percentage

        Parameters
        ----------
        playerName : str
            The last name of a player, title case

        Returns
        -------
        tuple
            A tuple containing a player's overall walk percentage, as well as walk
            percentage against LHP and RHP

        """
        player = FungoPlayer.getDataFrames(playerName)

        return (
            fStat.walkPct(player[1]),
            fStat.walkPct(player[2][0]),
            fStat.walkPct(player[2][1]),
        )

    def getKPct(playerName: str) -> tuple:
        """
        Getter method for a player's k percentage

        Parameters
        ----------
        playerName : str
            The last name of a player, title case

        Returns
        -------
        tuple
            A tuple containing a player's overall on base percentage, as well as k
            percentage against LHP and RHP

        """
        player = FungoPlayer.getDataFrames(playerName)

        return (
            fStat.strikeoutPct(player[1]),
            fStat.strikeoutPct(player[2][0]),
            fStat.strikeoutPct(player[2][1]),
        )
