# ***************************************************************************************************** #
#                                                                                                       #
#                                                                  :::::       :::::        :::         #
#    highest_even.py                                              +:+:+:+     +:+:+:+     :+:+:+        #
#                                                                +:+  :+:    +:+   :+:   +:+ +:+        #
#    By: rdidier- <didier.rda@gmail.com>                        #+#  +:+    #+#   +:+   +#+  +:+        #
#                                                              #+# #+#     #+#   #+#   +#+#+#+#+        #
#    Created: 2019/11/20 13:49:26 by rdidier-                 #+#   #+#   #+#   #+#   #+#    #+#        #
#    Updated: 2019/11/20 14:44:12 by rdidier-                ###   ###   ########    ###     ###.br     #
#                                                                                                       #
# ***************************************************************************************************** #

def highest_even(li):
    aux = []
    li.sort(reverse = True)
    aux = []
    for value in li:
        if (value % 2) == 0:
            aux.append(value)
    return (aux[0])
a = [1,2,3,15,13,8,222,4,5,6]
print(highest_even(a))