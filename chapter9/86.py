import pickle
from collections import defaultdict
from scipy import io
fname_t_func = "t_func"
out_fname = "86_out"
def _86():
    with open(fname_t_func, "rb") as f_data:
        t_func = pickle.load(f_data)

    t_index = defaultdict(int)

    for t_i, t in enumerate(t_func.keys()):
        t_index[t] = t_i

    matrix = io.loadmat("85")["matrix"]
    with open(out_fname,"w") as out_target:
        print(matrix[t_index["United_States"]], file=out_target)

if __name__ == "__main__":
    _86()

"""
4 * 75 = 300 次元
[ 5.13579070e-01  2.96913529e+00 -6.24637663e-01 -1.87945656e-01
  5.92164740e-01 -5.28746614e-01 -8.34080627e-01 -2.88819193e-01
  4.25463752e-02  1.51418276e+00  9.61783859e-02 -2.83677187e-01
 -2.09655561e+00 -2.41681912e-01 -1.51116368e+00  1.09708300e+00
 -2.56397718e+00 -4.10980206e-01  1.24045058e+00  1.75498666e-01
  9.68386503e-01 -8.69583557e-01 -1.11167604e-05 -5.66227224e-01
 -1.20710980e+00  1.71988252e-01  4.97966991e-01 -9.33390294e-02
  2.90542842e-01 -2.34091881e-02  3.85138337e-01  3.45822915e-01
 -3.99543296e-01  1.44527757e-02  1.93856308e-02  1.95621923e-01
 -9.19215252e-02 -2.78190960e-01 -2.11587375e-01 -5.01070956e-01
  3.75608867e-02  4.95177041e-01  5.07701700e-01 -1.35477882e-01
  3.51578509e-01  4.15559287e-02 -3.95114704e-01 -2.83668652e-01
  1.00290196e+00 -2.94702014e-01  8.40188490e-01  1.59138620e-01
 -8.58205075e-02  1.02563551e-01 -4.00586012e-01 -3.82659353e-01
  1.98871986e-01  7.06096351e-01 -6.73662065e-01 -4.16175786e-01
 -8.61242284e-01  1.53090070e-02  3.71486516e-02  6.69658500e-01
  1.86952165e+00  2.98689521e-01  1.45547446e+00 -4.83224323e-01
 -8.33866474e-01  6.01441400e-02  6.97585071e-01  2.33979213e-01
  1.10274207e-01  1.16171213e-01 -3.14869167e-01  2.39478422e-01
 -7.93634257e-03 -3.45153225e-01  5.37124834e-02  1.11509090e+00
 -5.02000574e-01  4.28328656e-01 -3.58737349e-02 -1.70628299e-02
  4.45773050e-01  3.40748897e-01  3.32505780e-02  1.24469456e-01
  9.61675942e-01 -6.36478225e-02 -5.58012572e-01 -2.57835650e-01
  6.52397223e-02  2.87177822e-01 -1.15162513e+00  8.12120737e-01
 -3.59315398e-01 -2.69151359e-01  3.03217299e-01 -1.46845870e-01
  6.16912296e-01  4.57734365e-01  1.88553169e-01 -3.23848001e-01
 -5.32747853e-02 -1.57008142e-01  9.00537962e-02 -1.07497948e-01
 -5.90738576e-02 -1.52145575e-01 -2.92086852e-02 -1.24848100e-01
 -3.65162356e-01  7.67099313e-01 -2.02019126e-01 -5.95026319e-02
 -4.02511444e-01  5.71130376e-02 -7.17505675e-02  1.00948533e-02
  7.73227637e-02  2.78772224e-01 -3.56471938e-01 -3.18328940e-01
  4.98645081e-02 -1.17874767e-01 -7.07570445e-01 -7.67261833e-01
  9.28201737e-01 -4.10652125e-02 -9.48824080e-01  5.18932933e-02
  8.66033319e-01 -5.58466522e-01  5.40704136e-01  9.03475741e-01
  1.61482466e-01  3.28689234e-01  1.05728432e+00 -4.40457735e-02
 -2.88678784e-01  1.87721185e-01  4.81672193e-01 -3.47192673e-01
  3.53480031e-01 -6.64810300e-01  9.87998288e-01  2.94665298e-01
 -6.05168273e-01  8.77608045e-01  7.96074751e-01 -3.46204899e-01
 -3.67814712e-01 -2.31676658e-01 -2.57172313e-01 -4.77373932e-02
 -2.61551218e-01 -6.18867410e-01  6.71144972e-01  9.60312960e-02
  8.54132039e-01  1.08188548e-01  3.15841082e-01  2.47801818e-01
  9.42433202e-01  5.47024630e-01 -2.50562659e-01  5.90092323e-02
  2.52818230e-01  9.15353743e-01 -3.94335590e-02 -4.41691548e-02
  1.67195741e-01 -1.83953603e-01 -1.53719806e-02  1.88178783e-01
  3.50253079e-01  4.53535181e-01 -2.75082159e-01 -5.33209437e-01
  6.83123437e-01 -3.13119377e-01 -2.71310704e-02 -9.70190959e-02
  3.07204109e-01  8.82798841e-01 -3.41266499e-01 -2.68296072e-01
 -9.51683023e-03  3.04058562e-01 -4.23396810e-01  1.60827488e-01
  1.87896791e-02 -7.86311601e-01  1.74198991e-01  4.55764682e-01
  1.61847939e-01 -2.39936615e-01 -2.57876358e-01  2.24042411e-02
 -2.51314298e-01  1.16109940e-01 -3.28003796e-01 -4.48073463e-01
 -2.49578170e-01 -5.04218258e-02 -3.35098081e-01  1.17770319e-01
 -1.14725715e-02  4.40195262e-01  3.43068538e-01  1.72503627e-01
 -4.60238361e-01 -7.79859032e-01  1.53826623e-01  4.23481309e-01
  1.10089444e-01  4.94257826e-01  3.42169169e-01 -1.94189508e-01
  5.64725952e-01 -2.10469934e-01 -3.36570655e-01 -1.97208842e-02
  2.36654493e-01  2.08906666e-03 -2.38972197e-01  3.15763366e-01
 -5.91810377e-01 -8.46347228e-02  2.97353080e-01 -2.15027115e-01
  2.65709862e-02 -1.56632057e-01  2.88904372e-01 -1.76590034e-01
  5.72141775e-01 -8.33355329e-02  1.03986269e-01  5.32832937e-04
 -7.25032466e-01  1.52946227e-01 -2.48039719e-01 -3.67814732e-01
 -4.12773718e-01 -1.38730333e-02 -6.97968614e-01  4.65602936e-01
 -2.22532803e-01 -1.47737440e-01 -7.37817149e-01  3.43007524e-01
  1.17509558e-01  3.68250598e-01 -5.81153061e-01 -7.41481776e-01
  2.40819364e-01 -1.60462203e-01 -2.93888510e-01  1.83103699e-01
 -6.43559740e-02  1.16684873e-01  1.65321133e-02  4.75391720e-01
  9.19361846e-02  7.78211231e-02 -1.53331785e-01  1.79921408e-01
  1.59579985e-01  7.87014194e-02  4.17925595e-01  2.29181433e-01
 -1.16521854e-02  1.12160868e-01 -8.86497106e-02 -1.95627496e-01
 -4.58175804e-01  5.53168648e-01 -3.64255674e-02  3.57840437e-01
 -3.29134889e-01  3.57760898e-01  9.96875969e-02 -2.86873390e-01
 -4.78974877e-01  1.28480850e-01 -2.98916342e-01 -4.10900037e-01
 -4.46242304e-01 -5.01018553e-01 -1.72803355e-01  1.89125504e-01
  4.82671543e-02  1.00818741e-01  4.96304277e-02  4.35394684e-02
  3.92143309e-01 -2.88682377e-01  1.03757668e-01 -5.55177501e-01]
"""