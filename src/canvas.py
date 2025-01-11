import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Canvas(Gtk.DrawingArea):
    """Draws the canvas"""

    def __init__(self, algorithm_manager):
        super().__init__()
        self.algorithm_manager = algorithm_manager
        self.connect("draw", self.on_draw)

    def on_draw(self, widget, cr):
        """Draws the dataset."""
        data = self.algorithm_manager.data
        width = self.get_allocated_width()
        height = self.get_allocated_height()
        bar_width = width / len(data)
        max_value = max(data)

        for i, value in enumerate(data):
            bar_height = (value / max_value) * height
            x = i * bar_width
            y = height - bar_height

            # Highlighting
            if i in self.algorithm_manager.highlight_indices:
                cr.set_source_rgb(0.8, 0.2, 0.2)  # Red for highlights
            else:
                cr.set_source_rgb(0.2, 0.4, 0.8)  # Blue for normal bars

            cr.rectangle(x, y, bar_width - 2, bar_height)
            cr.fill()


class StatusManager(Gtk.Label):
    """Manages the status bar messages."""

    def __init__(self):
        super().__init__()
        self.set_text("Select an algorithm and press Start.")

    def update_status(self, message):
        self.set_text(message)
