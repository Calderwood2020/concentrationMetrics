# encoding: utf-8

# (c) 2015-2017 Open Risk, all rights reserved
#
# Concentration Library is licensed under the MIT license a copy of which is included
# in the source distribution of TransitionMatrix. This is notwithstanding any licenses of
# third-party software included in this distribution. You may not use this file except in
# compliance with the License.
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.

import concentration_library as cl
import pandas as pd

dataset_path = cl.source_path + "datasets/"

# Comparison with R version in IC2 package on hhbudget dataset
# Expected Results:
# Epsilon 0: 0
# Epsilon 1: 0.3245925
# Epsilon 2: 0.4951668
# Epsilon 3: 0.6053387
# Epsilon 4: 0.6856425

hhbudgets = pd.read_csv(dataset_path + "hhbudgets.csv")
y = hhbudgets.as_matrix(columns=["ingreso"])
print(cl.atkinson(y, 0))
print(cl.atkinson(y, 1))
print(cl.atkinson(y, 2))
print(cl.atkinson(y, 3))
print(cl.atkinson(y, 4))