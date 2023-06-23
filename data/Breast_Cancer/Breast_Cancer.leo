program dt.aleo {
	struct Inputs {
		p1: u32,
		p2: u32,
		p3: u32,
		p4: u32,
		p5: u32,
		p6: u32,
		p7: u32,
		p8: u32,
		p9: u32,
	}
	// Code auto generated from DecisionTreeClassifier using dt_to_leo_code.py 
	transition main(inputs: Inputs) -> public u32 {
		if (inputs.p4 < 5u32) {
			if (inputs.p3 < 25u32) {
				if (inputs.p1 < 35u32) {
					if (inputs.p8 < 35u32) {
						return 0u32;
					} else {
						return 0u32;
					}
				} else {
					return 0u32;
				}
			} else {
				if (inputs.p7 < 5u32) {
					if (inputs.p2 < 15u32) {
						if (inputs.p8 < 25u32) {
							if (inputs.p1 < 55u32) {
								if (inputs.p1 < 45u32) {
									return 0u32;
								} else {
									if (inputs.p3 < 75u32) {
										if (inputs.p8 < 5u32) {
											if (inputs.p3 <= 50u32) {
												return 0u32;
											} else {
												return 0u32;
											}
										} else {
											if (inputs.p3 <= 60u32) {
												return 0u32;
											} else {
												return 1u32;
											}
										}
									} else {
										return 0u32;
									}
								}
							} else {
								return 0u32;
							}
						} else {
							if (inputs.p9 < 5u32) {
								return 1u32;
							} else {
								return 0u32;
							}
						}
					} else {
						if (inputs.p8 < 25u32) {
							if (inputs.p8 < 15u32) {
								if (inputs.p9 < 5u32) {
									return 0u32;
								} else {
									if (inputs.p1 < 45u32) {
										if (inputs.p3 < 65u32) {
											if (inputs.p1 < 35u32) {
												return 0u32;
											} else {
												if (inputs.p3 < 55u32) {
													if (inputs.p8 < 5u32) {
														if (inputs.p3 < 35u32) {
															return 1u32;
														} else {
															if (inputs.p3 < 45u32) {
																return 0u32;
															} else {
																return 0u32;
															}
														}
													} else {
														if (inputs.p3 < 35u32) {
															return 0u32;
														} else {
															return 0u32;
														}
													}
												} else {
													return 0u32;
												}
											}
										} else {
											if (inputs.p3 <= 90u32) {
												if (inputs.p3 < 75u32) {
													if (inputs.p1 < 35u32) {
														return 1u32;
													} else {
														return 0u32;
													}
												} else {
													return 1u32;
												}
											} else {
												return 0u32;
											}
										}
									} else {
										if (inputs.p3 < 35u32) {
											return 0u32;
										} else {
											return 0u32;
										}
									}
								}
							} else {
								if (inputs.p1 < 45u32) {
									if (inputs.p3 < 55u32) {
										return 1u32;
									} else {
										return 0u32;
									}
								} else {
									return 1u32;
								}
							}
						} else {
							return 0u32;
						}
					}
				} else {
					if (inputs.p3 < 35u32) {
						if (inputs.p1 < 45u32) {
							if (inputs.p2 <= 10u32) {
								return 0u32;
							} else {
								return 1u32;
							}
						} else {
							return 0u32;
						}
					} else {
						if (inputs.p1 < 55u32) {
							if (inputs.p3 < 75u32) {
								if (inputs.p9 < 5u32) {
									if (inputs.p1 < 45u32) {
										return 0u32;
									} else {
										return 1u32;
									}
								} else {
									if (inputs.p1 < 45u32) {
										if (inputs.p3 < 55u32) {
											if (inputs.p2 < 15u32) {
												return 1u32;
											} else {
												if (inputs.p3 < 45u32) {
													return 0u32;
												} else {
													if (inputs.p1 < 35u32) {
														return 0u32;
													} else {
														if (inputs.p8 < 5u32) {
															return 0u32;
														} else {
															if (inputs.p8 <= 20u32) {
																return 1u32;
															} else {
																return 0u32;
															}
														}
													}
												}
											}
										} else {
											if (inputs.p8 < 25u32) {
												if (inputs.p3 < 65u32) {
													return 1u32;
												} else {
													if (inputs.p8 <= 10u32) {
														return 1u32;
													} else {
														return 0u32;
													}
												}
											} else {
												return 0u32;
											}
										}
									} else {
										if (inputs.p8 < 35u32) {
											if (inputs.p2 < 15u32) {
												return 0u32;
											} else {
												if (inputs.p3 <= 60u32) {
													if (inputs.p8 < 15u32) {
														return 0u32;
													} else {
														return 0u32;
													}
												} else {
													return 0u32;
												}
											}
										} else {
											if (inputs.p3 <= 50u32) {
												return 1u32;
											} else {
												return 0u32;
											}
										}
									}
								}
							} else {
								return 0u32;
							}
						} else {
							if (inputs.p3 < 55u32) {
								if (inputs.p3 < 45u32) {
									if (inputs.p8 < 5u32) {
										return 0u32;
									} else {
										return 1u32;
									}
								} else {
									return 0u32;
								}
							} else {
								if (inputs.p1 < 65u32) {
									if (inputs.p8 < 5u32) {
										if (inputs.p9 < 5u32) {
											if (inputs.p3 <= 80u32) {
												return 1u32;
											} else {
												return 0u32;
											}
										} else {
											if (inputs.p3 <= 80u32) {
												return 0u32;
											} else {
												return 1u32;
											}
										}
									} else {
										return 1u32;
									}
								} else {
									return 0u32;
								}
							}
						}
					}
				}
			}
		} else {
			if (inputs.p7 < 5u32) {
				if (inputs.p9 < 5u32) {
					return 1u32;
				} else {
					if (inputs.p1 < 45u32) {
						if (inputs.p8 < 5u32) {
							return 0u32;
						} else {
							return 1u32;
						}
					} else {
						if (inputs.p8 <= 20u32) {
							if (inputs.p5 < 5u32) {
								if (inputs.p4 < 15u32) {
									return 0u32;
								} else {
									if (inputs.p1 < 55u32) {
										return 0u32;
									} else {
										return 1u32;
									}
								}
							} else {
								return 1u32;
							}
						} else {
							return 1u32;
						}
					}
				}
			} else {
				if (inputs.p8 < 5u32) {
					if (inputs.p3 < 55u32) {
						return 0u32;
					} else {
						if (inputs.p3 < 65u32) {
							return 1u32;
						} else {
							if (inputs.p9 < 5u32) {
								return 0u32;
							} else {
								return 1u32;
							}
						}
					}
				} else {
					if (inputs.p3 < 55u32) {
						if (inputs.p3 < 35u32) {
							return 0u32;
						} else {
							return 1u32;
						}
					} else {
						if (inputs.p1 < 45u32) {
							return 0u32;
						} else {
							if (inputs.p3 < 65u32) {
								return 0u32;
							} else {
								return 1u32;
							}
						}
					}
				}
			}
		}
	}
}