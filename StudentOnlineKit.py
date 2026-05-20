import PySimpleGUI as sg
import time
import math
from statistics import mean, median, mode

class Window1:
    def __init__(self):
        self.layout = [
            [sg.Text('This is Window 1')],
            [sg.Button('Open Calculator')],
            [sg.Button('Open Stop Watch')],
            [sg.Button('Probability')],
            [sg.Button('Compound Interest')],
            [sg.Button('Statistical Analysis')],
            [sg.Button('Triangle Solver')]
        ]
        self.window = sg.Window('Window 1', self.layout)

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Open Calculator':
                self.window.close()
                Calculator().run()
            if event == 'Open Stop Watch':
                self.window.close()
                StopWatch().run()
            if event == 'Probability':
                self.window.close()
                Probability().run()
            if event == 'Compound Interest':
                self.window.close()
                CompoundInterest().run()
            if event == 'Statistical Analysis':
                self.window.close()
                StatisticalAnalysis().run()
            if event == 'Triangle Solver':
                self.window.close()
                TriangleSolver().run()

class StopWatch:
    def __init__(self):
        self.layout = [
            [sg.Text('Stopwatch', font=('Helvetica', 20), justification='center')],
            [sg.Text('00:00:00', font=('Helvetica', 48), justification='center', key='-TIMER-')],
            [sg.Button('Start', size=(10, 2)), sg.Button('Pause', size=(10, 2)), sg.Button('Reset', size=(10, 2)), sg.Button('Go back', size=(5,2)),]

        ]

        window = sg.Window('Stopwatch', self.layout, finalize=True)

        running = False
        start_time = None
        paused_time = None
        total_paused_time = 0

        while True:
            event, values = window.read(timeout=10)

            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Start':
                if not running:
                    running = True
                    start_time = time.time()
                    paused_time = None
            elif event == 'Pause':
                if running:
                    running = False
                    paused_time = time.time()
            elif event == 'Reset':
                running = False
                start_time = None
                paused_time = None
                total_paused_time = 0
                window['-TIMER-'].update('00:00:00')
            elif event == 'Go back':
                window.close()
                Window1().run()

            if running:
                if paused_time is not None:
                    total_paused_time += time.time() - paused_time
                    paused_time = None

                elapsed_time = time.time() - start_time - total_paused_time
                hours = int(elapsed_time / 3600)
                minutes = int((elapsed_time % 3600) / 60)
                seconds = int(elapsed_time % 60)
                window['-TIMER-'].update('{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))

        window.close()

class Calculator:
    def __init__(self):
        self.layout = [
            [sg.Text('Enter first number:'), sg.InputText(key='-NUM1-')],
            [sg.Text('Enter second number:'), sg.InputText(key='-NUM2-')],
            [sg.Button('ADD'), sg.Button('SUBTRACT'), sg.Button('MULTIPLY'), sg.Button('DIVIDE')],
            [sg.Button('Go back', size=(5,2))]
        ]
        self.window = sg.Window('Calculator', self.layout)

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Go back':
                self.window.close()
                Window1().run()
            if event in ['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE']:
                num1 = float(values['-NUM1-'])
                num2 = float(values['-NUM2-'])
                if event == 'ADD':
                    result = num1 + num2
                elif event == 'SUBTRACT':
                    result = num1 - num2
                elif event == 'MULTIPLY':
                    result = num1 * num2
                elif event == 'DIVIDE':
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        result = 'Cannot divide by zero!'
                sg.popup('Result', result)

        self.window.close()

class Probability:
    def __init__(self):
        self.layout = [
            [sg.Text('Enter probability (between 0 and 1):'), sg.InputText(key='-PROB-')],
            [sg.Text('Enter number of events:'), sg.InputText(key='-EVENTS-')],
            [sg.Button('Calculate')],
            [sg.Button('Go back', size=(5,2))]
        ]
        self.window = sg.Window('Probability Calculator', self.layout)

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Go back':
                self.window.close()
                Window1().run()
            if event == 'Calculate':
                prob = float(values['-PROB-'])
                events = int(values['-EVENTS-'])
                result = prob ** events
                sg.popup('Result', result)

        self.window.close()

class CompoundInterest:
    def __init__(self):
        self.layout = [
            [sg.Text('Enter principal amount:'), sg.InputText(key='-PRINCIPAL-')],
            [sg.Text('Enter interest rate (in percentage):'), sg.InputText(key='-RATE-')],
            [sg.Text('Enter time (in years):'), sg.InputText(key='-TIME-')],
            [sg.Button('Calculate')],
            [sg.Button('Go back', size=(5,2))]
        ]
        self.window = sg.Window('Compound Interest Calculator', self.layout)

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Go back':
                self.window.close()
                Window1().run()
            if event == 'Calculate':
                principal = float(values['-PRINCIPAL-'])
                rate = float(values['-RATE-']) / 100
                time = float(values['-TIME-'])
                result = principal * ((1 + rate) ** time)
                sg.popup('Result', result)

        self.window.close()

class StatisticalAnalysis:
    def __init__(self):
        self.layout = [
            [sg.Text('Enter data (comma-separated):'), sg.InputText(key='-DATA-')],
            [sg.Button('Calculate')],
            [sg.Button('Go back', size=(5,2))]
        ]
        self.window = sg.Window('Statistical Analysis', self)
