import discord
from discord import Option



accountsregistar = {829023821494747166: {"<:bitcoinbtclogo:1113804083275513856> Bitcoin": "0xEC0456A49b45328c273E3202cc44DCadb49b169c", "<:EthereumETHicon:1113804166222069824> Ethereum": "0xEC0456A49b45328c273E3202cc44DCadb49b169c", "<:litecoinltclogo:1113804377031974942> Litecoin": "Lhw6zqCt9fRucBXaKV9Es7pzrFftvgNH7B", "<:paypal:1113886955734847568> Paypal": "https://paypal.me/funnyman01", "<:Cash_AppLogo:1113888203624173680> Cashapp": "£F12231"}, 1075992750207541398: {"<:bitcoinbtclogo:1113804083275513856> Bitcoin": "bc1q65ykyhfrn5jw78ql806a5ds5e46n0yqx4s56w2", "<:EthereumETHicon:1113804166222069824> Ethereum": "0x08Da5620dDA228D46649934A03776BD41b2A3F4a", "<:paypal:1113886955734847568> Paypal":"wock6s@protonmail.com", "<:Cash_AppLogo:1113888203624173680> Cashapp": "$Charles3s"}}

intents = discord.Intents.all()
bott = discord.Bot(intents=intents)

@bott.event
async def on_ready():
    print(f"Logged in as {bott.user}")
    await bott.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/wallets"))


@bott.slash_command()
async def wallets(ctx, user: Option(discord.Member, "The user you want to see the available payment methods of", required=True)):
    if user.id in accountsregistar.keys():
        Embed = discord.Embed(title=f"{user.name}'s Wallets", color=0xBC17DF)
        for i in accountsregistar[user.id].keys():
            Embed.add_field(name=i, value="``"+accountsregistar[user.id][i]+"``")
        await ctx.respond(embed=Embed)
    else:
        await ctx.respond("Invalid user selected", ephemeral=True)

if __name__ == "__main__":
    bott.run("")