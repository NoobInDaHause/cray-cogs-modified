winnerdm_message: str = (
    "You have won a giveaway!"
)

hostdm_message: str = (
    "Your giveaway has ended."
)

embed_title: str = "{prize}"
embed_description: str = (
    "React with {emoji} to enter.\n" "Hosted by: {host.mention}\n" "Ends: {timestamp}\n"
)
embed_footer_text: str = "Winners: {winners} | Ends at"
embed_footer_icon: str = "{host_avatar_url}"
embed_thumbnail: str = "{server_icon_url}"

guild_default_config = {
    "msg": "**:tada: GIVEAWAY :tada:**",
    "msg2": "**:tada: GIVEAWAY ENDED :tada:**",
    "emoji": "🎉",
    "winnerdm": False,
    "winnerdm_message": winnerdm_message,
    "hostdm": False,
    "hostdm_message": hostdm_message,
    "reactdm": False,
    "unreactdm": False,
    "endmsg": "Congratulations to the winner(s) above for winning the **{prize}** giveaway.", # "Congratulations to {winner}for winning the **{prize}** giveaway.\n{link}", "The giveaway for **{prize}** has ended.\nWinner(s): {winner}\n{link}"
    "tmsg": "Prize: **{prize}**\nDonator: {donor.mention}\n\nThank **{donor}** in general chat.",
    "manager": [],
    "pingrole": None,
    "autodelete": False,
    "blacklist": [],
    "bypass": [],
    "multi_roles": {},
    "top_managers": {},
    "show_defaults": True,
    "embed_title": embed_title,
    "embed_description": embed_description,
    "embed_footer_text": embed_footer_text,
    "embed_footer_icon": embed_footer_icon,
    "embed_thumbnail": embed_thumbnail,
    "color": None,
}

commands_to_delete = ["giveaway start", "giveaway flash", "giveaway end", "giveaway reroll"]
