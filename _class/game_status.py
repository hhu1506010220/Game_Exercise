class GameStatus():
    def __init__(self, ai_settings):
        # 初始化统计信息
        self.ai_settings = ai_settings
        self.reset_stats()
        # 初始为非活跃状态
        self.game_active = False

    def reset_stats(self):
        # 重置
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0