#!/usr/bin/python3
'''
Driver.py
Authors: Rafael Zamora
Last Updated: 2/18/17

'''

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from Qlearning4k import QLearnAgent
from Doom import Doom
from Models import DoomQModel

def train():
    '''
    '''
    # Parameters
    scenario = 'configs/rigid_turning.cfg'
    frame_skips = 6
    qlearn_param = {
        'nb_epoch' : 100,
        'steps' : 5000,
        'batch_size' : 50,
        'memory_size' : 10000,
        'nb_frames' : 3,
        'alpha' : 1.0,
        'gamma' : 0.9,
        'epsilon' : [1.0, 0.1],
        'epsilon_rate' : 0.5,
        'observe' : 10,
        'checkpoint' : 5,
        'filename' : 'rigid_turning_.h5'
    }

    #Initiates VizDoom Scenario
    doom = Doom('configs/rigid_turning.cfg', frame_skips=6)

    # Preform Q Learning on Scenario
    model = DoomQModel(resolution=doom.get_state().shape[-2:], nb_frames=qlearn_param['nb_frames'], nb_actions=len(doom.actions))
    agent = QLearnAgent(model, **qlearn_param)
    agent.train(doom)
    model.save_weights("rigid_turning.h5")

def play():
    '''
    Method used to show trained model playing Vizdoom Scenario.

    '''
    #Initiates VizDoom Scenario
    doom = Doom('configs/basic.cfg', frame_skips=0)

    # Run Scenario and play replay
    model = DoomQModel(resolution=doom.get_state().shape[-2:], nb_frames=qlearn_param['nb_frames'], nb_actions=len(doom.actions))
    agent = QLearnAgent(model)
    doom.run(agent, save_replay='basic.lmp', verbose=True)
    doom.replay('basic.lmp')


def test():
    '''
    Method used to test Vizdoom Scenarios with human player.

    '''
    #Initiates VizDoom Scenario and play
    doom = Doom('configs/rigid_turning.cfg')
    doom.replay('rigid_turning_.lmp')

if __name__ == '__main__':
    #train()
    test()
    #play()
