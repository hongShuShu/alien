class Settings():
    """游戏设置类"""

    def __init__(self):

        # 屏幕大小
        self.screen_width = 1200
        self.screen_height = 500
        self.bg_color = (230, 230, 230)
        
        # 飞船数量
        self.ship_limit = 3
            
        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        # 飞船停止速度
        self.fleet_drop_speed = 10
            
        # 飞船速度
        self.speedup_scale = 1.1
        self.score_scale = 1.5
    
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """动态初始化游戏设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
        self.alien_points = 50
    
        # 左边移是1 右边是-1
        self.fleet_direction = 1
        
    def increase_speed(self):
        """加速设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
