from discord_webhook import DiscordWebhook, DiscordEmbed

def push_webhooks(WEBHOOK_URL,user,source,room):
    webhook = DiscordWebhook(url=WEBHOOK_URL)
    title="**"+user[3]+"** vient de pawn la machine **"+room['title']+"**"
    embed = DiscordEmbed(title=title, color=source[3])
    embed.set_author(name=source[1],url=room["url"],icon_url=source[4])
    webhook.add_embed(embed)
    response = webhook.execute()