"""
run 'python visualizations.py' to generate the plots into 'media' folder
(you might get some warnings)
"""


from os import path

import matplotlib.pyplot as plt
import pandas as pd

# local modules
from utils import load_data


def _select_avg_question_type_scores(data: pd.DataFrame) -> pd.DataFrame:
    """
    This function compresses the information of each individual to his average
    scores on each of the 5 question types.

    Example
    ---------
    >>> # assuming there are only two question types: "EXT" and "CNS"
    >>> # and an extra column "Placeholder" which contains other info
    >>> data = pd.DataFrame(data=[[1,2,3,'some data type'],
                                [4,5,6, 'some data type'],
                                [7,8,9, 'some data type']],
                                columns=["EXT1", "EXT2", "CNS1", "Placeholder"])
    >>> select_avg_question_type_scores(data)
    pd.DataFrame(data=[[1.5,3],
                    [4.5,6],
                    [7.5,9]],
                    columns=['EXT_mean', 'CNS_mean'])
    """

    _df = data.copy()
    qtypes = ['EXT', 'EST', 'AGR', 'CSN', 'OPN']
    individual_mean_qtype_df = pd.DataFrame(index=_df.index)

    for question_type in qtypes:
        question_type_data = _df.filter(regex=f"{question_type}\d*$")
        question_type_mean = question_type_data.mean(axis=1)
        individual_mean_qtype_df[f'{question_type}_mean'] = question_type_mean
    return individual_mean_qtype_df


def plotGroupAverageDistribution(data: pd.DataFrame, save: bool, filename: str = None, n: int = 500):
    """
    'How different are the individuals when they are described by their average
    score on each group?'

    To answer this question, this function will plot a radviz. Each direction
    of the radviz will represent the average trait score out of the 5 well known
    traits. This way, each individual will be graphically represented as a point
    in all the 5 axis of the traits.

    Parameters
    ----------
    n: size of sample to plot
    (if everything is plotted it takes a long time to compute)
    """

    _df = data.copy()
    individual_mean_qtype_df = _select_avg_question_type_scores(_df)

    individual_mean_qtype_df['class'] = 'Placeholder'

    plt.figure(figsize=(10, 8))
    plt.title('Question type mean of each participant - RadVis')
    pd.plotting.radviz(individual_mean_qtype_df.iloc[:n], 'class', alpha=0.2)
    if save:
        if not filename:
            filename = 'participants_avg_qtype_radvis'

        plt.savefig(filename + '.png')


if __name__ == '__main__':

    data = load_data()
    print('data loaded')
    plotGroupAverageDistribution(data, save=True, filename=path.join(
        'media', 'participants_avg_qtype_radvis'), n=500)
    print('participants_avg_qtype_radvis.png - Done')
