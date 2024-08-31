import endstone.plugin
from endstone.command import Command, CommandSender
from endstone import ColorFormat


class RolePlayMessage(endstone.plugin.Plugin):
    api_version = "0.5"

    def on_load(self) -> None:
        self.logger.info("RP-Message load!")

    def on_enable(self) -> None:
        self.logger.info("RP-Message is enable!")

    def on_disable(self) -> None:
        self.logger.info("RP-Message is disable!")

    commands = {
        "e": {
            "description": "Simulation of chat actions for role-playing.",
            "usages": ["/e [msg: message]"],
            "permissions": ["rp_message.command.e"],
        }
    }

    permissions = {
        "rp_message.command.e": {
            "description": "Allow users to use the /e command.",
            "default": True,
        }
    }

    def on_command(self, sender: CommandSender, command: Command, args: list[str]) -> bool:
        if command.name == "e":
            if args[0] == "":
                sender.send_message(f"{ColorFormat.YELLOW}Usage /e (message)")
            else:
                sender.send_message(f"{sender.name} {ColorFormat.BOLD}{ColorFormat.GRAY}>> "
                                    f"{ColorFormat.RESET}{ColorFormat.LIGHT_PURPLE}{args[0]}{ColorFormat.RESET}")
        return True
