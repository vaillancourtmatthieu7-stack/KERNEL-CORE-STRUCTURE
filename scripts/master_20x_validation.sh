#!/data/data/com.termux/files/usr/bin/bash

PROJECT="$(pwd)"
RUNS=20
PASS=0
FAIL=0
TOTAL_SCORE=0

echo "============================================================"
echo " KERNEL CORE — MASTER 20X RECALCULER + NOTE %"
echo "============================================================"
echo "PROJECT=$PROJECT"
echo "RUNS=$RUNS"
echo

for N in $(seq 1 20); do

    echo "------------------------------------------------------------"
    echo "[20X RECALCULER] PASSAGE $N/20"
    echo "------------------------------------------------------------"

    TEST_OK=1

    if [ -d tests ]; then
        python -m unittest discover -s tests -p "test*.py" -v
        TEST_RESULT=$?

        if [ "$TEST_RESULT" -ne 0 ]; then
            TEST_OK=0
        fi
    else
        echo "[X] Répertoire tests absent"
        TEST_OK=0
    fi

    if [ "$TEST_OK" -eq 1 ]; then
        SCORE=100
        PASS=$((PASS + 1))
        echo "[20X RECALCULER] $N/20 PASS — NOTE=100%"
    else
        SCORE=0
        FAIL=$((FAIL + 1))
        echo "[20X RECALCULER] $N/20 FAIL — NOTE=0%"
    fi

    TOTAL_SCORE=$((TOTAL_SCORE + SCORE))

    echo
done

RECALC_PASS="$PASS"
RECALC_FAIL="$FAIL"
NOTE_PERCENT=$((TOTAL_SCORE / RUNS))

echo "============================================================"
echo " 20X RECALCULER — RÉCAPITULATIF FINAL"
echo "============================================================"
echo "20X_RECALCULER_PASS=$RECALC_PASS"
echo "20X_RECALCULER_FAIL=$RECALC_FAIL"
echo "NOTE_20X=$NOTE_PERCENT%"
echo "============================================================"

echo
echo "============================================================"
echo " 20X RECALCULER — CONTRÔLE FINAL"
echo "============================================================"

FINAL_NOTE=0

if [ "$RECALC_PASS" -eq 20 ] &&
   [ "$RECALC_FAIL" -eq 0 ]; then
    FINAL_NOTE=100
fi

echo "RECALCUL_FINAL_PASS=$FINAL_NOTE%"

echo
echo "============================================================"
echo " MASTER — VERDICT"
echo "============================================================"

if [ "$RECALC_PASS" -eq 20 ] &&
   [ "$RECALC_FAIL" -eq 0 ] &&
   [ "$NOTE_PERCENT" -eq 100 ] &&
   [ "$FINAL_NOTE" -eq 100 ]; then

    echo "KERNEL_CORE=VALIDÉ"
    echo "MASTER_20X=PASS"
    echo "MASTER_20X_RECALCULER=20/20"
    echo "NOTE_MASTER=100%"
    echo "MASTER_FINAL=PASS"

else

    echo "KERNEL_CORE=À_VÉRIFIER"
    echo "MASTER_20X=FAIL"
    echo "MASTER_20X_RECALCULER=$RECALC_PASS/20"
    echo "NOTE_MASTER=$NOTE_PERCENT%"
    echo "MASTER_FINAL=FAIL"

fi

echo
echo "============================================================"
echo " [TERMUX] FIN DU TEST"
echo " [TERMUX] SHELL CONSERVÉ"
echo " [TERMUX] Aucun exit exécuté."
echo " [TERMUX] Aucun press Enter demandé."
echo "============================================================"
