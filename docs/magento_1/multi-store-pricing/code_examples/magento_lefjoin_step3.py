if ($joinLeft) {
                $select->joinLeft($tableName, $joinCond, $colls);
            } else {
                $select->join($tableName, $joinCond, $colls);
}
