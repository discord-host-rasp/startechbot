
import time, re,sys
from discord.ext import commands
import discord,dislash,json
from dislash import InteractionClient, SelectMenu, SelectOption, Button, ButtonStyle, Option, OptionType, ActionRow, OptionChoice
from discord import Colour



# get the sys args from the command line
token = sys.argv[1] # token

prefix = 't.'

attributes = "{}.x = 300;\n {}.y = 100;\n {}.width = 200;\n {}.height = 160;"

owners = [673508396330123293]

bot = commands.Bot(command_prefix=prefix, help_command=None)

#Ideas for minigamesBot
"""
💬 Text Based Minigames
bent︲fasttype︲flip︲guessthenumber︲guessthepokemon︲hangman︲mirror︲randomcase︲randomcolor︲reverse︲sudo︲tiny︲vaporwave
🔘 Button(s) Minigames
2048︲chaoswords︲connect4︲fight︲lieswatter︲neverhaveiever︲pokemon︲quickclick︲rockpaperscissors︲shuffleguess︲snake︲tictactoe︲trivia︲uno︲willyoupressthebutton︲wouldyourather
🎙️ Voice Minigames
betrayal-io︲chess︲fishington-io︲poker-night︲youtubetogether
"""

"""
Games implemented:
Minesweeper, CoinFlip, GuessTheNumber, MemeGenerator, RandomColor, 8ball, reverse
"""
################################

# make a help_command array with the commands
help_command = {
    "help": "Shows this message",
    "ping": "Send the bot ping",
    "meme": "Generates some memes",
    "coin-flip": "Flips a coin",
    "guess-the-number": "Make a guess-the-number game",
    "minesweeper": "Play a Minesweeper",
    "random-color": "Sends a random color"}



@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

async def botpinged(message):
        if re.fullmatch(rf"<@!?{bot.user.id}>", message.content):
            return await message.channel.send(f"My prefix is `{prefix}` or you can use slash commands!")


@bot.event
async def on_message(msg):
    await botpinged(msg)




def open_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def dump_data(filename,data):
    with open(filename, "w") as f:
        json.dump(data,f)


# get the data from the json file
# and then add it 1
# and then dump it to the json file
def used_commands_count(ctx):
    data = open_json_file("info.json")
    data["cmd_count"] += 1
    dump_data("info.json",data)

async def make_rect(ShapeName,Shape, inter):
    embed=discord.Embed(title=f"Here is info about {Shape}")
    embed.add_field(name="Defining", value=f"{ShapeName} {Shape} = new {ShapeName}();", inline=False)
    embed.add_field(name="All attributes", value=attributes.format(Shape,Shape,Shape,Shape), inline=False)
    embed.add_field(name="Drawing", value=f"{Shape}.draw();", inline=False)
    return await inter.send(embed=embed)

from dislash import InteractionClient
inter_client = InteractionClient(bot)
# If 'test_guilds' param isn't specified, the commands are registered globally (up to 1 hour).

# commands

# rectangles
@inter_client.slash_command(
    name="object", # Defaults to the function name
    description="Give The Snippets About a specific object!",
    options=[
        Option(
            "object",
            description="Object to get info about",
            required=True,
            choices=[
                OptionChoice("Rect", "rect"),
                OptionChoice("Pentagon", "pentagon"),
                OptionChoice("Hexagon", "hexagon"),
                OptionChoice("Line", "line"),
                OptionChoice("Triangle", "triangle"),
                OptionChoice("Text", "text"),
                OptionChoice("Image", "image"),
                OptionChoice("Ellipse", "ellipse"),
            ]
        ),
        Option(
            "object_name",
            description="Object name",
            required=False,
        )
    ])
async def shape(inter,object,object_name=None):
    
    if object_name == None:
        if object == "rect":
            await make_rect("Rect", "rect", inter)
        if object == "pentagon":
            embed=discord.Embed(title="Here is info about Pentagon object")
            embed.add_field(name="Defining", value="Pentagon pentagon = new Pentagon();", inline=False)
            embed.add_field(name="All attributes", value="pentagon.x = 600;\npentagon.y = 350;\npentagon.radius = 70;\npentagon.brush = color(255,0, 255);\npentagon.pen = color(125,125,125);\npentagon.penThickness = 1;\npentagon.alpha = 255;", inline=False)
            embed.add_field(name="Drawing", value="pentagon.draw();", inline=False)
            await inter.send(embed=embed)
        if object == "hexagon":
            embed=discord.Embed(title="Here is info about Hexagon object")
            embed.add_field(name="Defining", value="Hexagon hexagon = new Hexagon();", inline=False)
            embed.add_field(name="All attributes", value="hexagon.x = 400;\nhexagon.y=250;\nhexagon.radius=150;\nhexagon.brush = color(0,0, 255);\nhexagon.penThickness = 1;\nhexagon.alpha = 200;", inline=False)
            embed.add_field(name="Drawing", value="hexagon.draw();", inline=False)
            await inter.send(embed=embed)
        if object == "line":
            embed=discord.Embed(title="Here is info about Line object")
            embed.add_field(name="Defining", value="Line line = new Line();", inline=False)
            embed.add_field(name="All attributes", value="line.x1 = 10;\nline.y1 = 10;\nline.x2 = 790;\nline.y2 = 10;\nline.pen = color(125,0,125);\nline.penThickness = 5;\nline.alpha = 255;", inline=False)
            embed.add_field(name="Drawing", value="line.draw();", inline=False)
            await inter.send(embed=embed)
        if object == "triangle":
            embed=discord.Embed(title="Here is info about Triangle object")
            embed.add_field(name="Defining", value="Triangle triangle = new Triangle();", inline=False)
            embed.add_field(name="All attributes", value="triangle.x1 = 10;\ntriangle.y1 = 10;\ntriangle.x2 = 100;\ntriangle.y2 = 10;\ntriangle.x3 = 100;\ntriangle.y3 = 100;\ntriangle.pen = color(0,255,125);\ntriangle.brush = color(125,0,125);\ntriangle.penThickness = 5;\ntriangle.alpha = 255;", inline=False)
            embed.add_field(name="Drawing", value="triangle.draw();", inline=False)
            await inter.send(embed=embed)
        if object == "text":
            embed=discord.Embed(title="Here is info about Text object")
            embed.add_field(name="Defining", value="Text txt1 = new Text();", inline=False)
            embed.add_field(name="All attributes", value="txt1.x = 100;\ntxt1.y = 150;\ntxt1.brush = color(255,0,0);\ntxt1.alpha = 255;\ntxt1.text = \"Hello\";\ntxt1.textSize = 150;\ntxt1.font = \"Arial\";", inline=False)
            embed.add_field(name="Drawing", value="txt1.draw();", inline=False)
            await inter.send(embed=embed)
        if object == "image":
            embed=discord.Embed(title="Here is info about Image object")
            embed.add_field(name="Defining", value="Image image = new Image();", inline=False)
            embed.add_field(name="All attributes", value="image.x = 100;\nimage.y = 100;\nimage.setImage(\"dog.png\");", inline=False)
            embed.add_field(name="Drawing", value="image.draw();", inline=False)
            await inter.send(embed=embed)
        if object == "ellipse":
            embed=discord.Embed(title="Here is info about Ellipse object")
            embed.add_field(name="Defining", value="Ellipse ellipse = new Ellipse();", inline=False)
            embed.add_field(name="All attributes", value="ellipse.x = 200;\nellipse.y = 150;\nellipse.radiusX = 100;\nellipse.radiusY = 100;\nellipse.brush = color(0,255, 0);\nellipse.pen = color(0, 0, 255);\nellipse.penThickness = 1;\nellipse.alpha = 230;", inline=False)
            embed.add_field(name="Drawing", value=" ellipse.draw();", inline=False)
            await inter.send(embed=embed)
        return used_commands_count(inter)
    
    if object == "rect":
            await make_rect("Rect", object_name, inter)
    if object == "pentagon":
            embed=discord.Embed(title="Here is info about Pentagon object")
            embed.add_field(name="Defining", value=f"Pentagon {object_name} = new Pentagon();", inline=False)
            embed.add_field(name="All attributes", value=f"{object_name}.x = 600;\n{object_name}.y = 350;\{object_name}.radius = 70;\n{object_name}.brush = color(255,0, 255);\n{object_name}.pen = color(125,125,125);\n{object_name}.penThickness = 1;\n{object_name}.alpha = 255;", inline=False)
            embed.add_field(name="Drawing", value=f"{object_name}.draw();", inline=False)
            await inter.send(embed=embed)
    if object == "hexagon":
            embed=discord.Embed(title="Here is info about Hexagon object")
            embed.add_field(name="Defining", value=f"Hexagon {object_name} = new Hexagon();", inline=False)
            embed.add_field(name="All attributes", value=f"{object_name}.x = 400;\n{object_name}.y=250;\n{object_name}.radius=150;\n{object_name}.brush = color(0,0, 255);\n{object_name}.penThickness = 1;\n{object_name}.alpha = 200;", inline=False)
            embed.add_field(name="Drawing", value=f"{object_name}.draw();", inline=False)
            await inter.send(embed=embed)
    if object == "line":
            embed=discord.Embed(title="Here is info about Line object")
            embed.add_field(name="Defining", value=f"Line {object_name} = new Line();", inline=False)
            embed.add_field(name="All attributes", value=f"{object_name}.x1 = 10;\n{object_name}.y1 = 10;\n{object_name}.x2 = 790;\n{object_name}.y2 = 10;\n{object_name}.pen = color(125,0,125);\n{object_name}.penThickness = 5;\n{object_name}.alpha = 255;", inline=False)
            embed.add_field(name="Drawing", value=f"{object_name}.draw();", inline=False)
            await inter.send(embed=embed)
    if object == "triangle":
            embed=discord.Embed(title="Here is info about Triangle object")
            embed.add_field(name="Defining", value=f"{object_name} triangle = new Triangle();", inline=False)
            embed.add_field(name="All attributes", value=f"{object_name}.x1 = 10;\n{object_name}.y1 = 10;\n{object_name}.x2 = 100;\n{object_name}.y2 = 10;\n{object_name}.x3 = 100;\n{object_name}.y3 = 100;\n{object_name}.pen = color(0,255,125);\n{object_name}.brush = color(125,0,125);\n{object_name}.penThickness = 5;\n{object_name}.alpha = 255;", inline=False)
            embed.add_field(name="Drawing", value=f"{object_name}.draw();", inline=False)
            await inter.send(embed=embed)
    if object == "text":
            embed=discord.Embed(title="Here is info about Text object")
            embed.add_field(name="Defining", value=f"Text {object_name} = new Text();", inline=False)
            embed.add_field(name="All attributes", value=f"{object_name}.x = 100;\n{object_name}.y = 150;\n{object_name}.brush = color(255,0,0);\n{object_name}.alpha = 255;\n{object_name}.text = \"Hello\";\n{object_name}.textSize = 150;\n{object_name}.font = \"Arial\";", inline=False)
            embed.add_field(name="Drawing", value=f"{object_name}.draw();", inline=False)
            await inter.send(embed=embed)
    if object == "image":
            embed=discord.Embed(title="Here is info about Image object")
            embed.add_field(name="Defining", value=f"Image {object_name} = new Image();", inline=False)
            embed.add_field(name="All attributes", value=f"{object_name}.x = 100;\n{object_name}.y = 100;\n{object_name}.setImage(\"dog.png\");", inline=False)
            embed.add_field(name="Drawing", value=f"{object_name}.draw();", inline=False)
            await inter.send(embed=embed)
    if object == "ellipse":
            embed=discord.Embed(title="Here is info about Ellipse object")
            embed.add_field(name="Defining", value=f"Ellipse {object_name} = new Ellipse();", inline=False)
            embed.add_field(name="All attributes", value=f"{object_name}.x = 200;\n{object_name}.y = 150;\n{object_name}.radiusX = 100;\n{object_name}.radiusY = 100;\n{object_name}.brush = color(0,255, 0);\n{object_name}.pen = color(0, 0, 255);\n{object_name}.penThickness = 1;\n{object_name}.alpha = 230;", inline=False)
            embed.add_field(name="Drawing", value=f"{object_name}.draw();", inline=False)
            await inter.send(embed=embed)
    return used_commands_count(inter)



# reverse command!
@inter_client.slash_command(
    name="method", # Defaults to the function name
    description="Give The Snippets About A Specific Method!",
    options=[
        Option(
            "method",
            description="Method to get info about",
            required=True,
            choices=[
                OptionChoice("Music", "music"),
                OptionChoice("Directions", "directions"),
            ]
        ),
        Option(
            "method_name",
            description="Method name",
            required=False,
        )
    ]
)
async def methods(inter, method,method_name=None):
    
    if method_name == None:
        if method == "directions":
            embed=discord.Embed(title="Here is info about Direction object")
            embed.add_field(name="All Directions", value="Direction.UP\nDirection.DOWN\nDirection.RIGHT\nDirection.LEFT\nDirection.UPRIGHT\nDirection.UPLEFT\nDirection.DOWNRIGHT\nDirection.DOWNLEFT", inline=True)
            await inter.send(embed=embed)
        if method == "music":
            embed=discord.Embed(title="Here is info about Music object")
            embed.add_field(name="Defining", value="Music music = new Music();", inline=False)
            embed.add_field(name="All attributes", value="music.loop = true;\nmusic.load(\"elvis.mp3\");\nmusic.play();", inline=False)
            await inter.send(embed=embed)
            return used_commands_count(inter)
    
    if method == "directions":
            embed=discord.Embed(title="Here is info about Direction object")
            embed.add_field(name="All Directions", value="Direction.UP\nDirection.DOWN\nDirection.RIGHT\nDirection.LEFT\nDirection.UPRIGHT\nDirection.UPLEFT\nDirection.DOWNRIGHT\nDirection.DOWNLEFT", inline=True)
            await inter.send(embed=embed)
    if method == "music":
            embed=discord.Embed(title="Here is info about Music object")
            embed.add_field(name="Defining", value=f"Music {method_name} = new Music();", inline=False)
            embed.add_field(name="All attributes", value=f"{method_name}.loop = true;\n{method_name}.load(\"elvis.mp3\");\n{method_name}.play();", inline=False)
            await inter.send(embed=embed)
    
    return used_commands_count(inter)

@inter_client.slash_command(
    name="ping", # Defaults to the function name
    description="Sends the bot ping!",
)
async def ping(ctx):
    
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")
    
    used_commands_count(ctx)


# developer commands
@inter_client.slash_command(
    name="dev", # Defaults to the function name
    description="Sends info about the bot dev!",
)
async def dev(ctx):
    embed = discord.Embed(title="Info ABout My Developer", description="his tag: Noma4321#0035\nhis id: 673508396330123293\nping: <@673508396330123293>", color=0xff0000)
    await ctx.send(embed=embed)
    
    used_commands_count(ctx)


@inter_client.slash_command(
    name="shutdown", # Defaults to the function name
    description="Shuts down the bot!",
)
async def shutdown(ctx):
    if ctx.author.id not in owners:
        return ctx.send("You are not my owner!\nonly owners are allowed to shut down the bot!")
    await ctx.send("Shutting down...")
    await bot.close()


# random color command
@inter_client.slash_command(
    name="randomcolor", # Defaults to the function name
    description="Sends a random color",
    
)
async def randomcolor(inter):
    
    # Make a hex to rgb function
    def HexToRgb(hex):
        hex = hex.lstrip('#')
        return tuple(int(hex[i:i+2], 16) for i in (0, 2 ,4))
    color = Colour.random()
    rgb = HexToRgb(str(color))
    embed = discord.Embed(title="Here is a random color", color=color)
    embed.add_field(name="Hex", value=str(color), inline=False)
    embed.add_field(name="Rgb", value=rgb, inline=False)
    
    await inter.send(embed=embed)
    
    used_commands_count(inter)

# color info command
@inter_client.slash_command(
    name="colorinfo", # Defaults to the function name
    description="Sends a random color",
    options=[
        Option(
        "color", "Enter the color you want to visualize.",
        OptionType.STRING,
        required=True)
    ]
)
async def ColorInfo(inter, color):
    
    if "#" in color:
        color = color.lstrip('#')
    # Make a hex to rgb function
    def HexToRgb(hex):
        return tuple(int(hex[i:i+2], 16) for i in (0, 2 ,4))
    # get the format hex of color
    color = str(color)
    color = int(color, 16)
    rgb = HexToRgb(str(color))
    embed = discord.Embed(title="Here is a random color", color=color)
    embed.add_field(name="Hex", value=color, inline=False)
    embed.add_field(name="Rgb", value=rgb, inline=False)
    
    await inter.send(embed=embed)
    
    used_commands_count(inter)


try:
    bot.run(token)
except:
    print("Pls make sure the token is working and all configured correctly")
