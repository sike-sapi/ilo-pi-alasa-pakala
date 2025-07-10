import discord

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=[1372566140110508143])
async def hello(ctx):
    await ctx.respond("Hello!")

@bot.slash_command(guild_ids=[1372566140110508143])
async def submit(ctx):
    modal = SubmitModal(title="Sentence submission")

    # Send the prompt for the sentence
    await ctx.send_modal(modal)
    await modal.wait()

    print(vars(modal))

    submission = modal.children[0].value
    channel = bot.get_channel(1392972779971678452)
    resp = await channel.send(
        content=f"{ctx.user.mention} li pana e toki ni:\n"
        f"> {submission}\n"
        "sona ale pi lipu pana:\n"
        "```python\n"
        f"{vars(modal)}\n"
        "```",
    )

class SubmitModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_item(
            discord.ui.InputText(
                label="Your sentence here!",
                max_length=200,
                style=discord.InputTextStyle.long,
                required=True,
            )
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            content="mi pana e toki sina tawa lawa ma! lawa li wile lukin e toki sina. o awen.\n"
            "I submitted your sentence to the overlords! Please wait for approval.",
            ephemeral=True,
        )
        self.stop()

bot.run('')
