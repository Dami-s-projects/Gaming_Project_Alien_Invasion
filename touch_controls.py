import pygame

class TouchControls:
    """Simple on-screen touch controls for mobile"""
    
    def __init__(self, screen_setting, screen):
        self.screen = screen
        self.screen_setting = screen_setting
        
        # Button size
        btn_size = 80
        margin = 20
        
        # D-pad buttons (bottom left)
        base_x = margin + btn_size
        base_y = screen_setting.screen_height - margin - btn_size * 2
        
        self.buttons = {
            'left': pygame.Rect(margin, base_y, btn_size, btn_size),
            'right': pygame.Rect(margin + btn_size * 2, base_y, btn_size, btn_size),
            'up': pygame.Rect(base_x, base_y - btn_size, btn_size, btn_size),
            'down': pygame.Rect(base_x, base_y + btn_size, btn_size, btn_size),
        }
        
        # Fire button (bottom right) - bigger
        self.buttons['fire'] = pygame.Rect(
            screen_setting.screen_width - margin - btn_size * 2,
            screen_setting.screen_height - margin - btn_size * 2,
            btn_size * 2,
            btn_size * 2
        )
        
        # Track which buttons are pressed
        self.pressed = {key: False for key in self.buttons}
        
        # Track active finger touches
        self.active_touches = {}
        
        # Font
        self.font = pygame.font.SysFont(None, 32)
    
    def handle_event(self, event):
        """Handle touch/mouse events. Returns 'fire' if fire button was just pressed."""
        fire_pressed = False
        
        
        if event.type == pygame.FINGERDOWN:
            x = event.x * self.screen_setting.screen_width
            y = event.y * self.screen_setting.screen_height
            button = self._get_button_at(x, y)
            if button:
                self.active_touches[event.finger_id] = button
                self.pressed[button] = True
                if button == 'fire':
                    fire_pressed = True
                    
        elif event.type == pygame.FINGERUP:
            if event.finger_id in self.active_touches:
                button = self.active_touches.pop(event.finger_id)
                # Only release if no other finger is on this button
                if button not in self.active_touches.values():
                    self.pressed[button] = False
                    
        elif event.type == pygame.FINGERMOTION:
            x = event.x * self.screen_setting.screen_width
            y = event.y * self.screen_setting.screen_height
            new_button = self._get_button_at(x, y)
            old_button = self.active_touches.get(event.finger_id)
            
            if old_button != new_button:
                if old_button and old_button not in [v for k,v in self.active_touches.items() if k != event.finger_id]:
                    self.pressed[old_button] = False
                if new_button:
                    self.pressed[new_button] = True
                self.active_touches[event.finger_id] = new_button
        
        # Also handle mouse for testing on desktop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            button = self._get_button_at(*event.pos)
            if button:
                self.active_touches['mouse'] = button
                self.pressed[button] = True
                if button == 'fire':
                    fire_pressed = True
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            if 'mouse' in self.active_touches:
                button = self.active_touches.pop('mouse')
                self.pressed[button] = False
        
        return fire_pressed
    
    def _get_button_at(self, x, y):
        """Return which button is at position, or None"""
        for name, rect in self.buttons.items():
            if rect.collidepoint(x, y):
                return name
        return None
    
    def apply_to_ship(self, ship):
        """Apply touch controls to ship movement (OR with keyboard)"""
        if self.pressed['left']:
            ship.moving_left = True
        if self.pressed['right']:
            ship.moving_right = True
        if self.pressed['up']:
            ship.moving_up = True
        if self.pressed['down']:
            ship.moving_down = True
    
    def draw(self, game_active):
        """Draw touch buttons when game is active"""
        if not game_active:
            return
        
        # Semi-transparent surface
        overlay = pygame.Surface(
            (self.screen_setting.screen_width, self.screen_setting.screen_height),
            pygame.SRCALPHA
        )
        
        # Draw d-pad
                # Draw d-pad with arrow shapes
        for name in ['left', 'right', 'up', 'down']:
            rect = self.buttons[name]
            color = (150, 150, 150, 180) if self.pressed[name] else (100, 100, 100, 120)
            pygame.draw.rect(overlay, color, rect, border_radius=10)
            pygame.draw.rect(overlay, (200, 200, 200, 150), rect, 3, border_radius=10)
            
            # Draw arrow shape
            cx, cy = rect.center
            arrow_color = (255, 255, 255)
            if name == 'left':
                points = [(cx+15, cy-15), (cx-15, cy), (cx+15, cy+15)]
            elif name == 'right':
                points = [(cx-15, cy-15), (cx+15, cy), (cx-15, cy+15)]
            elif name == 'up':
                points = [(cx-15, cy+15), (cx, cy-15), (cx+15, cy+15)]
            elif name == 'down':
                points = [(cx-15, cy-15), (cx, cy+15), (cx+15, cy-15)]
            pygame.draw.polygon(overlay, arrow_color, points)
        
        # Draw fire button
        fire_rect = self.buttons['fire']
        fire_color = (200, 50, 50, 180) if self.pressed['fire'] else (150, 30, 30, 120)
        pygame.draw.rect(overlay, fire_color, fire_rect, border_radius=15)
        pygame.draw.rect(overlay, (255, 100, 100, 150), fire_rect, 3, border_radius=15)
        
        fire_label = self.font.render('FIRE', True, (255, 255, 255))
        fire_rect_center = fire_label.get_rect(center=fire_rect.center)
        overlay.blit(fire_label, fire_rect_center)
        
        self.screen.blit(overlay, (0, 0))
