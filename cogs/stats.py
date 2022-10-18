import json
import time
import discord


class stats(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def stats(self, ctx):
        ok = await ctx.respond(embed=discord.Embed(description="Checking the Stats", color=discord.Color.yellow()))
        time.sleep(2)
        async def get_data_data():
            with open(f"data.json", "r", encoding='utf8') as f:
                data = json.load(f)

            return data

        datatype = await get_data_data()
        usesmine = datatype["minesuse"]
        title = f"Stratus Predictor"
        color = discord.Color.green()
        desc = f"**Mines**\n```{usesmine}```\n**Crash**\n```Not implemented Yet```"
        em = discord.Embed(description=desc, color=color, title=title)
        await ok.edit_original_message(embed=em)



def setup(bot):
    bot.add_cog(stats(bot))