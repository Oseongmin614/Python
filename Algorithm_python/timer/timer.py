import tkinter as tk
from tkinter import messagebox
import math
import sys
import os
from plyer import notification

DARK_BACKGROUND = "#2C3E50"
WORK_STATE_RED = "#E74C3C"
BREAK_STATE_GREEN = "#2ECC71"
LONG_BREAK_LIGHT_GREEN = "#66BB6A"
BUTTON_BG = BREAK_STATE_GREEN
BUTTON_ACTIVE_BG = "#27AE60"
LIGHT_TEXT = "white"
PROGRESS_BAR_BG_GREY = "#4A6278"
FONT_NAME = "맑은 고딕"

class PomodoroTimer:
    def __init__(self, window):
        self.window = window
        self.window.title("타타타닥타닥타이머")
        self.window.config(padx=20, pady=15, bg=DARK_BACKGROUND)

        self.reps = 0
        self.timer = None
        self.total_seconds = 0

        self.title_label = tk.Label(text="타이머", fg=BREAK_STATE_GREEN, bg=DARK_BACKGROUND, font=(FONT_NAME, 30, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=3, pady=5)

        self.canvas = tk.Canvas(width=160, height=180, bg=DARK_BACKGROUND, highlightthickness=0)
        self.progress_bg = self.canvas.create_oval(5, 5, 155, 155, fill="", outline=PROGRESS_BAR_BG_GREY, width=8)
        self.progress_arc = self.canvas.create_arc(5, 5, 155, 155, start=90, extent=0, style=tk.ARC,
                                                   outline=BREAK_STATE_GREEN, width=8)
        self.timer_text = self.canvas.create_text(80, 85, text="00:00", fill=LIGHT_TEXT, font=(FONT_NAME, 28, "bold"))
        self.canvas.grid(row=1, column=0, columnspan=3, pady=5)

        settings_frame = tk.Frame(bg=DARK_BACKGROUND)
        settings_frame.grid(row=2, column=0, columnspan=3, pady=(5, 10))

        tk.Label(settings_frame, text="작업:", bg=DARK_BACKGROUND, fg=LIGHT_TEXT, font=(FONT_NAME, 9)).pack(side=tk.LEFT, padx=(0, 2))
        self.work_entry = tk.Entry(settings_frame, width=3, font=(FONT_NAME, 9), bg=DARK_BACKGROUND, fg=LIGHT_TEXT, insertbackground=LIGHT_TEXT)
        self.work_entry.insert(0, "25")
        self.work_entry.pack(side=tk.LEFT, padx=(0, 8))

        tk.Label(settings_frame, text="휴식:", bg=DARK_BACKGROUND, fg=LIGHT_TEXT, font=(FONT_NAME, 9)).pack(side=tk.LEFT, padx=(0, 2))
        self.break_entry = tk.Entry(settings_frame, width=3, font=(FONT_NAME, 9), bg=DARK_BACKGROUND, fg=LIGHT_TEXT, insertbackground=LIGHT_TEXT)
        self.break_entry.insert(0, "5")
        self.break_entry.pack(side=tk.LEFT, padx=(0, 8))

        tk.Label(settings_frame, text="긴 휴식:", bg=DARK_BACKGROUND, fg=LIGHT_TEXT, font=(FONT_NAME, 9)).pack(side=tk.LEFT, padx=(0, 2))
        self.long_break_entry = tk.Entry(settings_frame, width=3, font=(FONT_NAME, 9), bg=DARK_BACKGROUND, fg=LIGHT_TEXT, insertbackground=LIGHT_TEXT)
        self.long_break_entry.insert(0, "20")
        self.long_break_entry.pack(side=tk.LEFT, padx=(0, 8))

        tk.Label(settings_frame, text="SET:", bg=DARK_BACKGROUND, fg=LIGHT_TEXT, font=(FONT_NAME, 9)).pack(side=tk.LEFT, padx=(0, 2))
        self.sets_entry = tk.Entry(settings_frame, width=3, font=(FONT_NAME, 9), bg=DARK_BACKGROUND, fg=LIGHT_TEXT, insertbackground=LIGHT_TEXT)
        self.sets_entry.insert(0, "4")
        self.sets_entry.pack(side=tk.LEFT)

        self.start_button = tk.Button(text="시작", font=(FONT_NAME, 10, "bold"), highlightthickness=0,
                                      bg=BUTTON_BG, fg=LIGHT_TEXT,
                                      activebackground=BUTTON_ACTIVE_BG, activeforeground=LIGHT_TEXT,
                                      relief="flat", borderwidth=0,
                                      command=self.start_timer)
        self.start_button.grid(row=3, column=0, pady=5, ipadx=5)

        self.reset_button = tk.Button(text="재설정", font=(FONT_NAME, 10, "bold"), highlightthickness=0,
                                      bg=BUTTON_BG, fg=LIGHT_TEXT,
                                      activebackground=BUTTON_ACTIVE_BG, activeforeground=LIGHT_TEXT,
                                      relief="flat", borderwidth=0,
                                      command=self.reset_timer)
        self.reset_button.grid(row=3, column=2, pady=5, ipadx=5)

        self.check_marks = tk.Label(fg=BREAK_STATE_GREEN, bg=DARK_BACKGROUND, font=(FONT_NAME, 15, "bold"))
        self.check_marks.grid(row=4, column=0, columnspan=3)

        # 저작권 표시 추가
        self.copyright_label = tk.Label(text="© o.s.m", fg="#7F8C8D", bg=DARK_BACKGROUND, font=(FONT_NAME, 8))
        self.copyright_label.grid(row=5, column=0, columnspan=3, pady=(5, 0))

    def get_time_settings(self):
        try:
            work_min = int(self.work_entry.get())
            short_break_min = int(self.break_entry.get())
            long_break_min = int(self.long_break_entry.get())
            sets_count = int(self.sets_entry.get())

            if sets_count <= 0:
                raise ValueError("SET 값은 1 이상이어야 합니다.")

            return work_min, short_break_min, long_break_min, sets_count
        except ValueError as e:
            messagebox.showerror("입력 오류", f"시간 또는 SET 값은 숫자로 입력해주세요. ({e})")
            return None, None, None, None

    def reset_timer(self):
        if self.timer:
            self.window.after_cancel(self.timer)
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.canvas.itemconfig(self.progress_arc, extent=0)
        self.title_label.config(text="타이머", fg=BREAK_STATE_GREEN)
        self.check_marks.config(text="")
        self.reps = 0
        self.start_button.config(state="normal")

    def start_timer(self):
        self.start_button.config(state="disabled")
        work_min, short_break_min, long_break_min, sets_count = self.get_time_settings()
        if work_min is None:
            self.start_button.config(state="normal")
            return

        self.reps += 1

        notification_title = "뽀모도로 타이머"
        notification_message = ""

        if self.reps % (sets_count * 2) == 0:
            self.total_seconds = long_break_min * 60
            self.title_label.config(text="긴 휴식", fg=LONG_BREAK_LIGHT_GREEN)
            self.canvas.itemconfig(self.progress_arc, outline=LONG_BREAK_LIGHT_GREEN)
            notification_message = "긴 휴식 시간입니다! 편안하게 쉬세요."
        elif self.reps % 2 == 0:
            self.total_seconds = short_break_min * 60
            self.title_label.config(text="휴식", fg=BREAK_STATE_GREEN)
            self.canvas.itemconfig(self.progress_arc, outline=BREAK_STATE_GREEN)
            notification_message = "짧은 휴식 시간입니다! 가볍게 쉬세요."
        else:
            self.total_seconds = work_min * 60
            self.title_label.config(text="작업", fg=WORK_STATE_RED)
            self.canvas.itemconfig(self.progress_arc, outline=WORK_STATE_RED)
            notification_message = "작업 시간입니다! 집중해서 업무하세요."

        notification.notify(
            title=notification_title,
            message=notification_message,
            app_name="뽀모도로",
            timeout=10
        )

        self.count_down(self.total_seconds)

    def count_down(self, count):
        count_min = math.floor(count / 60)
        count_sec = count % 60
        self.canvas.itemconfig(self.timer_text, text=f"{count_min:02d}:{count_sec:02d}")

        progress_percentage = (self.total_seconds - count) / self.total_seconds
        angle = progress_percentage * 360
        self.canvas.itemconfig(self.progress_arc, extent=angle)

        if count > 0:
            self.timer = self.window.after(1000, self.count_down, count - 1)
        else:
            self.start_timer()

            if self.reps % 2 != 0:
                marks = "✔" * (math.floor(self.reps / 2) + 1)
                self.check_marks.config(text=marks)

            if (self.reps - 1) % (self.get_time_settings()[3] * 2) == 0 and self.reps > 1:
                self.check_marks.config(text="")

if __name__ == "__main__":
    window = tk.Tk()
    app = PomodoroTimer(window)
    window.mainloop()

