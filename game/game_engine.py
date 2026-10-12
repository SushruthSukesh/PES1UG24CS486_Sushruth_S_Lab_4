import pygame
from game.deck import Deck

class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.deck = Deck()

        self.current_card = self.deck.draw()
        self.next_card = None
        self.score = 0
        self.streak = 0
        self.reveal_until = 0
        self.status_msg = "Will the next card be HIGHER or LOWER?"
        self.status_color = (220, 220, 220)

        btn_w, btn_h = 190, 54
        self.btn_higher = pygame.Rect(width // 2 - btn_w - 18, height - 85, btn_w, btn_h)
        self.btn_lower = pygame.Rect(width // 2 + 18, height - 85, btn_w, btn_h)

        self.font_title = pygame.font.SysFont("segoeui", 38, bold=True)
        self.font_stat = pygame.font.SysFont("segoeui", 24, bold=True)
        self.font_medium = pygame.font.SysFont("segoeui", 28, bold=True)
        self.font_small = pygame.font.SysFont("segoeui", 20)
        self.font_label = pygame.font.SysFont("segoeui", 17, bold=True)

    def evaluate_guess(self, guess):
        """Draws next card and evaluates prediction."""
        if self.next_card is not None:
            return

        self.next_card = self.deck.draw()
        current_rank = self.current_card.numeric_rank
        next_rank = self.next_card.numeric_rank

        if next_rank == current_rank:
            self.status_msg = f"PUSH! Both cards are {self.current_card.rank_str}"
            self.status_color = (245, 210, 80)
        else:
            correct = (
                next_rank > current_rank
                if guess == "HIGHER"
                else next_rank < current_rank
            )

            if correct:
                self.streak += 1
                points = self.streak
                self.score += points
                self.status_msg = (
                    f"CORRECT! +{points} point{'s' if points != 1 else ''} "
                    f"(streak {self.streak})"
                )
                self.status_color = (80, 220, 80)
            else:
                self.streak = 0
                self.score = max(0, self.score - 1)
                self.status_msg = (
                    f"WRONG! {self.next_card.rank_str} vs "
                    f"{self.current_card.rank_str}"
                )
                self.status_color = (235, 75, 75)

        self.reveal_until = pygame.time.get_ticks() + 700

    def _finish_reveal(self):
        if self.next_card is not None and pygame.time.get_ticks() >= self.reveal_until:
            self.current_card = self.next_card
            self.next_card = None

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.next_card is not None:
                return
            if self.btn_higher.collidepoint(event.pos):
                self.evaluate_guess("HIGHER")
            elif self.btn_lower.collidepoint(event.pos):
                self.evaluate_guess("LOWER")

    def update(self):
        self._finish_reveal()

    def render(self, screen):
        screen.fill((18, 55, 42))
        pygame.draw.rect(screen, (24, 91, 65), (0, 0, self.width, 112))
        pygame.draw.line(screen, (72, 170, 120), (28, 111), (self.width - 28, 111), 2)

        title_surf = self.font_title.render("HIGH-LOW", True, (250, 250, 245))
        screen.blit(title_surf, (self.width // 2 - title_surf.get_width() // 2, 20))
        subtitle = self.font_small.render("Predict the next card", True, (184, 222, 204))
        screen.blit(subtitle, (self.width // 2 - subtitle.get_width() // 2, 67))

        self._draw_stat(screen, "SCORE", str(self.score), 48, 27, (255, 218, 92))
        self._draw_stat(screen, "STREAK", str(self.streak), 165, 27, (255, 218, 92))
        self._draw_stat(screen, "CARDS LEFT", str(self.deck.remaining), self.width - 125, 27, (220, 240, 230))

        card_w, card_h = 150, 210
        card_y = 145
        if self.next_card is None:
            self.current_card.render(
                screen, self.width // 2 - card_w // 2, card_y, card_w, card_h
            )
        else:
            self.current_card.render(screen, self.width // 2 - card_w - 35, card_y, card_w, card_h)
            self.next_card.render(screen, self.width // 2 + 35, card_y, card_w, card_h)
            arrow = self.font_title.render("→", True, (245, 245, 245))
            screen.blit(arrow, (self.width // 2 - arrow.get_width() // 2, card_y + 85))

        label = self.font_label.render(
            "CURRENT CARD" if self.next_card is None else "CURRENT                 REVEALED",
            True, (154, 201, 180)
        )
        screen.blit(label, (self.width // 2 - label.get_width() // 2, 362))

        status_surf = self.font_medium.render(self.status_msg, True, self.status_color)
        screen.blit(status_surf, (self.width // 2 - status_surf.get_width() // 2, 397))

        self._draw_button(screen, self.btn_higher, (39, 157, 82), "HIGHER")
        self._draw_button(screen, self.btn_lower, (188, 62, 67), "LOWER")

    def _draw_stat(self, screen, label, value, center_x, y, color):
        label_surface = self.font_label.render(label, True, (178, 214, 197))
        value_surface = self.font_stat.render(value, True, color)
        screen.blit(label_surface, (center_x - label_surface.get_width() // 2, y))
        screen.blit(value_surface, (center_x - value_surface.get_width() // 2, y + 27))

    def _draw_button(self, screen, rect, color, text):
        pygame.draw.rect(screen, color, rect, border_radius=12)
        pygame.draw.rect(screen, (230, 245, 237), rect, width=2, border_radius=12)
        high_surf = self.font_medium.render(text, True, (255, 255, 255))
        screen.blit(
            high_surf,
            (rect.centerx - high_surf.get_width() // 2, rect.centery - high_surf.get_height() // 2),
        )
