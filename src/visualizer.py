import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
from .algo_manager import AlgorithmManager
from .canvas import Canvas, StatusManager


class AlgorithmVisualizer(Gtk.Window):
    """Main application class."""

    def __init__(self):
        super().__init__(title="Algorithm Visualizer")
        # self.set_border_width(10)
        self.set_default_size(800, 600)

        # Components
        self.algorithm_manager = AlgorithmManager()
        self.canvas = Canvas(self.algorithm_manager)
        self.status_manager = StatusManager()

        # Layout
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(self.main_box)

        # Toolbar
        self.toolbar = Gtk.Box(spacing=10)
        self.main_box.pack_start(self.toolbar, False, False, 0)

        # Algorithm selection
        self.dropdown = Gtk.ComboBoxText()
        for algo in self.algorithm_manager.sorting_algos.keys():
            self.dropdown.append_text(algo)
        self.dropdown.set_active(0)
        self.toolbar.pack_start(self.dropdown, False, False, 0)

        # Buttons
        self.start_button = Gtk.Button(label="Start")
        self.start_button.connect("clicked", self.start_sorting)
        self.toolbar.pack_start(self.start_button, False, False, 0)

        self.reset_button = Gtk.Button(label="Reset")
        self.reset_button.connect("clicked", self.reset_visualizer)
        self.toolbar.pack_start(self.reset_button, False, False, 0)

        # Canvas and Status
        self.main_box.pack_start(self.canvas, True, True, 0)
        self.main_box.pack_start(self.status_manager, False, False, 0)

        # Initialize
        # self.reset_visualizer()

    def reset_visualizer(self, widget):
        """Reset the dataset."""
        self.algorithm_manager.reset_data()
        self.status_manager.update_status("Visualizer has been reset.")
        self.canvas.queue_draw()

    def start_sorting(self, widget):
        """Start the sorting animation."""
        if self.algorithm_manager.get_generator(self.dropdown.get_active_text()):
            self.algorithm_manager.highlight_indices = (-1, -1)
            generator = self.algorithm_manager.get_generator(
                self.dropdown.get_active_text()
            )
            print(self.dropdown.get_active_text())
            print(generator)
            self.animate_sorting(generator)

    def animate_sorting(self, generator):
        """Animate the sorting process."""

        def step():
            try:
                next(generator)
                self.status_manager.update_status(self.algorithm_manager.status_message)
                self.canvas.queue_draw()
                return True
            except StopIteration:
                self.status_manager.update_status("Sorting complete!")
                return False

        GLib.timeout_add(int(20), step) # Edit number for speed
